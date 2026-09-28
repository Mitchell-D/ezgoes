"""
Tool for querying and downloading from the GOES AWS bucket

The bucket keys are organized as:

noaa-goes{sat}/{sensor}-{level}-{scan}/{yyyy}/{doy}/{HH}

With files:

OR_{var}_G{sat}_s{start_time}_e{end_time}_c{create_time}.nc

with some file name variance based on the specific product invoked.
"""

import json
import s3fs
from pathlib import Path
from datetime import datetime,timedelta

from SatelliteProduct import SatelliteProduct

class GetGOES:
    def __init__(self, menu_file:Path=None, refetch:bool=False):
        self._s3 = None
        self._products = None
        self._valid_sats = {"16", "17", "18"}
        self._s3_key = "noaa-goes{satellite}/{product}/{yyyy}/{doy}/{hh}"

        if menu_file is None or not menu_file.exists() or refetch:
            self._products = self._get_product_menu()
            if not menu_file is None:
                json.dump(
                    [tuple(sp) for sp in self._products],
                    menu_file.open("w")
                    )
        else:
            self._products = [
                SatelliteProduct(*p) for p in json.load(menu_file.open("r"))
                ]

        self._valid = {
            "satellite":tuple(self._valid_sats),
            "sensor":tuple(set(p.sensor for p in self._products)),
            "level":tuple(set(p.level for p in self._products)),
            "scan":tuple(set(p.scan for p in self._products)),
            }

    @property
    def s3(self):
        """
        Return the s3 api object as a property, and only fetch it once if
        it is needed. This prevents re-connecting for each download, and
        prevents unneccesary connection when the config is being used.
        """
        if self._s3 is None:
            self._s3 = s3fs.S3FileSystem(anon=True)
        return self._s3

    def __iter__(self):
        for v in (self.satellite, self.sensor, self.level, self.scan):
            yield v

    def _get_product_menu(self):
        """
        Queries the NOAA GOES S3 bucket and returns a list of all available
        products as instances of SatelliteProduct. This makes it
        easy to search for available products by attribute.

        This method relies on the NOAA product naming convention described here
        https://github.com/awslabs/open-data-docs/blob/main/docs/noaa/noaa-goes16/

        in which products are named by dash-separated strings like:
        [instrument]-[processing_level]-[product]

        :@return: list of GOES_Product objects for available bucket subdirs
        """
        products = []
        for sat in self._valid_sats:
            for r in self.s3.ls(f"noaa-goes{sat}", refresh=True):
                tmp = r.split("/")[-1].split("-")
                # index.html is listed along with products; skip anything that
                # doesn't conform to the 3-field standard
                if len(tmp) != 3:
                    continue
                sensor,level,scan = tmp
                products.append(SatelliteProduct(sat, sensor, level, scan))
        return products

    def validate(self, satellite=None, sensor=None, level=None, scan=None):
        """
        Make sure the provided options are available in the product menu,
        returning a list of options that fit al the given constraints
        """
        satellite = str(satellite) if not satellite is None else None
        sensor = str(sensor) if not sensor is None else None
        level = str(level) if not level is None else None
        scan = str(scan) if not scan is None else None
        cand = self._products
        if satellite:
            if satellite not in self._valid["satellite"]:
                raise ValueError(
                        f"Provided satellite {satellite} is not one"
                        f" of the valid options {self._valid['satellite']}")
            cand = [c for c in cand if c.satellite==satellite]

        if sensor:
            if sensor not in self._valid["sensor"]:
                raise ValueError(
                        f"Provided sensor {sensor} is not one"
                        f" of the valid options {self._valid['sensor']}")
            cand = [c for c in cand if c.sensor==sensor]

        if level:
            if level not in self._valid["level"]:
                raise ValueError(
                        f"Provided level {level} is not one"
                        f" of the valid options {self._valid['level']}")
            cand = [c for c in cand if c.level==level]

        if scan:
            if scan not in self._valid["scan"]:
                raise ValueError(
                        f"Provided scan {scan} is not one"
                        f" of the valid options {self._valid['scan']}")
            cand = [c for c in cand if c.scan==scan]
        return cand

    def search(self, product:SatelliteProduct, start_time:datetime,
            end_time:datetime=None, substrings:str=[""],
            valid_window_hours=2):
        """
        Search the GOES AWS bucket for data files available for download
        using either a target time or time range. Files are specified by
        a single unique product, and optional substrings used to identify
        individual variables by the second underscore-separated field in the
        file name.

        If more than one substring is provided, returns a dict mapping
        the substring to a list of dicts describing all files containing the
        substring which are in the time range, or closest to start_time if no
        end_time is providd.

        The returned per-file dicts contain the s3 key of the file, its
        label field (second underscore-separated in the file name), the
        product tuple, and the start time of the file.

        :@param product: Specific SatelliteProduct to search for
        :@param start_time: Target time or initial time to look for
        :@param end_time: End of time window to consider valid
        :@param substrings: Components of file names to return (variables)
        :@param valid_window_hours: If no end_time is provided, the closest
            file within this number of hours of start_time will be returned
        """
        ## validate the product argument to identify a single SatelliteProduct
        if not isinstance(product, SatelliteProduct):
            assert isinstance(product, (tuple,list)), \
                "If a SatelliteProduct isn't provided, it must be a 4-tuple"
            product = SatelliteProduct(*list(map(str, product)))
        sprod = self.validate(*tuple(product))
        if len(sprod) > 1:
            raise ValueError(
                f"All SatelliteProduct fields must be defined:",
                tuple(product)
                )
        sprod = sprod[0]

        if isinstance(substrings, str):
            substrings = [substrings]

        ## determine search range based on whether end_time is provided
        return_closest = end_time is None
        if return_closest:
            t0 = start_time - timedelta(hours=valid_window_hours)
            tf = start_time + timedelta(hours=valid_window_hours)
        else:
            t0 = start_time
            tf = end_time
        assert t0 < tf, f"Start time must be before end time: {(t0, tf)}"

        ## enumerate all in-range hours
        check_hours = [
            t0 + timedelta(hours=i)
            for i in range(int((tf-t0).total_seconds()//3600) + 1)
            ]

        pkey = "-".join(tuple(sprod)[1:])
        avail = {}
        matched_keys = []
        for h in check_hours:
            s3k = self._s3_key.format(
                satellite=sprod.satellite,
                product=pkey,
                yyyy=h.strftime("%Y"),
                doy=h.strftime("%j"),
                hh=h.strftime("%H"),
                )
            try:
                for p in self.s3.ls(s3k):
                    _,label,_,stime,_,_ = Path(p).name.split("_")
                    for s in substrings:
                        if not s in label:
                            continue
                        if not s in avail.keys():
                            avail[s] = []
                        avail[s].append({
                            "product":tuple(sprod),
                            "stime":datetime.strptime(stime, "s%Y%j%H%M%S%f"),
                            "label":label,
                            "key":p,
                            })
                        if p in matched_keys:
                            print(f"WARNING: multiple substrings match {p}:",
                                f"{substrings=}")
            except FileNotFoundError:
                continue

        ## if a range request was made, go ahead and return all results
        if not return_closest:
            if len(avail.keys()) == 1:
                return avail[list(avail.keys())[0]]
            return avail

        ## otherwise, build a dict mapping each substring to the closest
        ## file(s) matching that substring
        closest = {}
        for s,alist in avail.items():
            for a in alist:
                cur_dt = abs(a["stime"] - start_time)
                if not s in closest.keys():
                    closest[s] = (cur_dt, [a])
                    continue
                ## skip if already found closer
                if cur_dt > closest[s][0]:
                    continue
                ## append if matching time
                elif cur_dt == closest[s][0]:
                    closest[s][1].append(a)
                ## replace if closer than before
                else:
                    closest[s] = (cur_dt, [a])

        closest = {k:v[1] for k,v in closest.items()}
        if len(closest.keys()) == 1:
            return closest[list(closest.keys())[0]]
        return closest
