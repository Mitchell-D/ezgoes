import s3fs
from pathlib import Path
from datetime import datetime
from datetime import timedelta

from .TextFormat import TextFormat as TF
from .goes_info import GOES_Product, GOES_File
from .goes_info import goes_descriptions, goes_products

class GetGOES:
    """
    Wrapper class on the NOAA AWS S3 bucket API for GOES. This class provides
    methods for searching the bucket for GOES satellite products, identifying
    available files in a specified time range, and downloading them files.
    """
    def __init__(self, refetch_api:bool=False):
        """
        Initialize a GetGOES class by making a connection to the

        :@param refetch_api:
        """
        self._s3 = None
        self._valid_satellites = {"16", "17", "18"}

        # Either load the products from the config, or
        self._products = self._get_product_api() if refetch_api \
                else  goes_products

        # Dictionary of valid options for product constraints
        self._valid = {
                "satellite":tuple(self._valid_satellites),
                "sensor":tuple(set(p.sensor for p in self._products)),
                "level":tuple(set(p.level for p in self._products)),
                "scan":tuple(set(p.scan for p in self._products)),
                }

    @property
    def s3(self):
        """
        Return the s3 api object as a property, and only fetch it once if
        it is needed.
        """
        if self._s3 is None:
            self._s3 = s3fs.S3FileSystem(anon=True)
        return self._s3

    def valid_product_fields(self, product_field:str=None):
        """
        Provided a product field in {"satellite", "sensor", "level", "scan"},
        returns a list of all valid options. For example, "satellite" will
        return ["16", "17", "18"] for each GOES generation.

        By default, returns a dict mapping every attribute to a list of its
        valid options.

        :@param product_field: One of {"satellite", "sensor", "level", "scan"}
        """
        if product_field is None:
            return self._valid
        assert product_field in self._valid.keys()
        return self._valid[product_field]

    def products(self, refetch_api:bool=False):
        """
        Returns all valid GOES_Product objects. If requested, queries the NOAA
        AWS bucket for all available GOES products.

        :@param refetch_api: If True, re-queries the AWS S3 bucket for products
        :@return: List of valid GOES_Product objects:
        """
        if refetch_api:
            return self._get_product_api()
        return self._products

    def product_tuples(self, refetch_api:bool=False):
        """
        Returns all valid products as a tuple as specified below

        :@param refetch_api: If True, re-queries the AWS S3 bucket for products
        :@return: Valid GOES_Product objects as tuples of strings like:
            (satellite, sensor, level, scan).
        """
        if refetch_api:
            return list(map(tuple, self._get_product_api()))
        return list(map(tuple, self._products))

    def download(self, file:GOES_File, data_dir:Path, replace=False):
        """
        Download the provided GOES_File from the AWS S3 bucket to the provided
        directory, keeping the file's default naming convention.

        :@param file: GOES_File with a path to a valid AWS bucket location.
        :@param data_dir: Directory to deposit downloaded netCDF file
        :@param replace: If True, existing files with the same name will be
            overwritten by a newly-downloaded version
        """
        new_path = data_dir.joinpath(Path(file.path).name)
        if new_path.exists() and not replace:
            print(TF.RED(f"{new_path.as_posix()} exists already; skipping."))
        else:
            print(TF.BLUE(f"Downloading to ", bright=True),
                  TF.WHITE(new_path.as_posix(), bright=True))
            self.s3.download(file.path, new_path.as_posix())
        return new_path

    def _get_product_api(self):
        """
        Queries the NOAA GOES S3 bucket and returns a list of all available
        products as instances of the GOES_Product namedtuple. This makes it
        easy to search for available products by attribute.

        This method relies on the NOAA product naming convention described here
        https://github.com/awslabs/open-data-docs/blob/main/docs/noaa/noaa-goes16/

        in which products are named by dash-separated strings like:
        [instrument]-[processing_level]-[product]

        :@return: list of GOES_Product objects for available bucket subdirs
        """
        products = []
        for satellite in self._valid_satellites:
            for r in self.s3.ls(f"noaa-goes{satellite}", refresh=True):
                tmp = r.split("/")[-1].split("-")
                # index.html is listed along with products; skip anything that
                # doesn't conform to the 3-field standard
                if len(tmp) != 3:
                    continue
                sensor, level, scan = tmp
                products.append(GOES_Product(satellite, sensor, level, scan))
        return products

    def search_products(self,satellite=None,sensor=None,level=None,scan=None):
        """
        Return a list of available products given a series of constraints
        """
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

    def search_hour(self, product:GOES_Product, target_time:datetime,
                  label_substr:str=None):
        """
        List all of the available files for the provided product within the
        provided UTC hour. Many products are sub-divided by a label which is
        the second underscore-separated field of the filenames. If the
        optional desired label is provided, the search will be further
        restricted to files that match the label.

        :@param product: valid GOES_Product namedtuple.
        """
        if any(p is None for p in product):
            raise ValueError(f"Provided product has a None field: {product}")
        product_key = "-".join((product.sensor, product.level, product.scan))
        s3_path = "noaa-goes{sat}/{product}/{year}/{jday}/{hour}".format(
                sat=product.satellite,
                product=product_key,
                year=target_time.strftime("%Y"),
                jday=target_time.strftime("%j"),
                hour=target_time.strftime("%H"),
                )
        paths = []
        for path in self.s3.ls(s3_path):
            _,label,_,timestr,_,_ = Path(path).name.split("_")
            if label_substr and label_substr not in label:
                continue
            paths.append(GOES_File(
                product=product,
                stime=datetime.strptime(timestr, "s%Y%j%H%M%S%f"),
                label=label,
                path=path,
                ))
        return paths

    def search_range(self, product:GOES_Product, init_time:datetime,
                   final_time:datetime, label_substr:str=None):
        """
        List all files with start times for the specified product falling
        within the provided range, with an inclusive init_time and exclusive
        final_time.

        :@param product: valid GOES_Product namedtuple.
        :@param init_time: Inclusive initial start time of files to return.
            Start time is the 4th field of the NOAA naming standard.
        :@param final_time: Exclusive final start time of files to return.
            Start time is the 4th field of the NOAA naming standard.
        :@param label_substr: Optional string label to restrict search results.
            The label is the second field of the NOAA naming standard, and
            typically denotes channels or scan modes.
        """
        assert init_time < final_time
        dhours = (final_time-init_time).total_seconds()//(60*60)
        tmp_time = datetime(init_time.year, init_time.month,
                            init_time.day, init_time.hour)
        files = []
        while tmp_time<final_time:
            files += self.search_hour(product, tmp_time, label_substr)
            tmp_time += timedelta(hours=1)

        files = [f for f in sorted(files,key=lambda f:f.stime)
                 if init_time<=f.stime and f.stime<final_time]
        return files

    def search_closest_to_time(self, product:GOES_Product, target_time:datetime,
                            label_substr:str=None, time_window_hrs=4):
        """
        Returns a list of products with the closest start time to the requested
        time.

        :@param product: Valid GOES_Product object with all fields filled out.
        :@param target_time: Desired start time of returned GOES_File object.
        :@param label_substr: bands and derived products are identified by a
            label in the 2nd underscore-separated field of the netCDF file
            name. If label_substr is a substring of one of these, only the
            files with the corresponding label are returned.
        :@param time_window_hrs: breadth of time window in which to search for
            files. May be useful for more transient products.
        """
        # All fields in the GOES_Product must be filled out
        assert all(product)
        start = target_time-timedelta(hours=time_window_hrs/2)
        end = target_time+timedelta(hours=time_window_hrs/2)
        files = self.search_range(product, start, end, label_substr)
        # If a label is provided, constrain files by substring
        if label_substr:
            files = [f for f in files if label_substr in f.label]
        # Get a list of time differences and return the minimum
        diffs = [abs((f.stime-target_time).total_seconds()) for f in files]
        closest = [files[i] for i in range(len(files)) if diffs[i]==min(diffs)]
        return closest

def describe(product:GOES_Product, do_print=False):
    """
    Pretty-print product descriptions if available in goes_info.py,
    returning None in every case. If you need the string version of
    descriptions, import the goes_info module directly instead of using
    an instance of the GetGOES class.

    :@param product: valid product to describe
    """
    prod_str = "-".join(product[1:])
    if prod_str not in goes_descriptions.keys():
        desc = ""
        print_str = TF.RED(f"(Missing description)", bright=True)
    else:
        desc = goes_descriptions[prod_str]
        print_str = TF.WHITE(desc, bright=True)
    if do_print:
        print(TF.BLUE(f"{product.satellite}-{prod_str:<16}",
                      bright=True)+print_str)
    return desc

def search_goes(query:GOES_Product=None, time:datetime=None,
                search_window:timedelta=None, goesapi:GetGOES=None,
                label_substr:str=None):
    """
    Pretty-prints product or file search results along with useful information.
    This method is meant to serve as a user interface to help narrow down
    product and file selection in accordance with the AWS API format.

    Use a GetGOES object and a GOES_Product query to either...
    (1) List GOES product options given constraints in the query.
    (2) Return a list of GOES_File objects for valid downloadable netCDFs
        if a specific product query is given (valid, with no None fields).

    GOES_Product valid options:
    satellite: ("16", "17", "18") # or None
    sensor:    ("ABI", "SUVI", "SEIS", "EXIS", "MAG", "GLM") # or None
    level:     ("L1b", "L2") # or None
    scan:      # Many options. Set provided query.scan to None for a listing.

    :@param query: GOES_Product object, which is a namedtuple with string
        fields for satellite, sensor, level, and scan. If some of the fields
        are set to None, a list of valid products will be returned. Otherwise
        if all query fields are provided and valid, a list of avai
    :@param goesapi: (Optional) existing GetGOES() instance. When a GetGOES()
        object is initialized, it fetches valid product options by querying
        the S3 bucket. Providing an existing object saves time since a new
        get request doesn't need to be made.
    :@param time: If a full valid product is specified by the query, time
        parameter sets a search target time. If no search_window is provided,
        the function returns all files with a stime closest to provided time.
    :@param search_window: Timedelta object added to the 'time' parameter to
        describe a time range in which to return files. This may be negative
        to describe a window
    """
    goesapi = GetGOES() if goesapi is None else goesapi
    query = GOES_Product(None, None, None, None) if query is None else query
    # If the product has None fields, search for and describe valid products.
    if not all(query):
        TF.YELLOW(f"Printing product descriptions for {query}", bold=True)
        products = goesapi.search_products(**query._asdict())
        for p in products:
            describe(p, do_print=True)
        return products
    # Otherwise, search for the product within the provided time bounds
    else:
        if query not in goesapi.products():
            raise ValueError(f"Provided product isn't a valid option")
        if time is None:
            raise ValueError(
                    f"You must provide a time to search for files")
        if search_window is None:
            files = goesapi.search_closest_to_time(
                    product=query,
                    target_time=time,
                    label_substr=label_substr,
                    )
            for f in files:
                print(TF.YELLOW(f.stime.strftime("%Y%m%d %H:%M ")),
                      Path(f.path).name)
            if not files:
                return []
            # All returned files will have the same start time
            time = files[0].stime
            print(TF.BLUE("\nFound data at time ") + TF.WHITE(time))
            print(TF.BLUE("With unique labels: "),
                  sorted(list(set([ f.label for f in files]))))
        else:
            # If the provided search window is negative, it should be the
            # initial time in the search range.
            init_time, final_time = tuple(sorted([time, time+search_window]))
            files = goesapi.search_range(
                    product=query,
                    init_time=init_time,
                    final_time=final_time,
                    label_substr=label_substr,
                    )
            if not files:
                return []
            all_times = sorted(list(set([ f.stime for f in files])))
            for f in files:
                print(TF.YELLOW(f.stime.strftime("%Y%m%d %H:%M ")),
                      Path(f.path).name)
            print(TF.BLUE("\nFound data in time range ") +
                  TF.WHITE(f"[{all_times[0]}, {all_times[-1]}]"))
            print(TF.BLUE("With unique labels: "),
                          sorted(list(set([ f.label for f in files]))))
    return files

if __name__=="__main__":
    GG = GetGOES()
    GG.download(
            GG.search_closest_to_time(
                product=GOES_Product(
                    satellite="16",
                    sensor="ABI",
                    level="L1b",
                    scan="RadC",
                    ),
                target_time=datetime.utcnow(),
                label_substr="C13",
                )[0],
            data_dir=Path("./"),
            )
    exit(0)

    """
    Call the search_goes method with no arguments to print a list of
    available products and their descriptions.
    The printed product strings are dash-separated fields SENSOR-LEVEL-SCAN,
    most of which are available for all 3 satellites.
    """
    search_goes()

    """
    You can provide a GOES_Product without all of its fields to search for
    product types that fit the constraints.
    """
    search_goes(GOES_Product(satellite="16", sensor="ABI", level="L2"))

    """
    Once you determine what product you want, specify a time range using a
    target time, and a search_window range around that time to look for data.

    satellite: ('16', '18', '17')
    sensor: ('MAG', 'SEIS', 'SUVI', 'EXIS', 'GLM', 'ABI')
    level: ('L1b', 'L2')
    scan: (many; use search_goes to find options)
    """
    files = search_goes(
            # Specify a GOES_Product to search for
            query=GOES_Product("16", "ABI", "L2", "CMIPC"),
            # Search for all files in the previous day
            time=datetime.utcnow(),
            search_window=timedelta(minutes=-30),
            label_substr="C13",
            )
    """
    If you've specified the right range of files to download, provide a
    download location in data_dir and call the GetGOES class' download method
    on each GOES_File object returned by search_goes.
    """
    data_dir = Path("./abi_data")

    GG = GetGOES()
    assert data_dir.exists()
    for f in files:
        GG.download(f, data_dir, replace=False)

