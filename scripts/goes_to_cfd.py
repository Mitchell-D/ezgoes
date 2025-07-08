
import h5py
import numpy as np
import argparse
from pathlib import Path
from datetime import datetime,timedelta

from ezgoes import GetGOES,search_goes,GOES_Product,GOES_File
from ezgoes.acquire import acquire_abi

def parse_args():
    parser = argparse.ArgumentParser(
        prog="ezgoes",
        usage="download and subset GOES satellite data"
    )
    parser.add_argument(
            #"-g",
            #"--goes_version",
            "goes_version",
            nargs="?",
            default="-",
            choices=["-","16","17","18"],
            #required=False,
            #dest="goes_version",
            type=str,
            help="GOES satellite version (ie 16, 17, 18)"
            )
    parser.add_argument(
            #"-i",
            #"--instrument",
            "instrument",
            nargs="?",
            #default="ABI",
            default="-",
            choices=["-","ABI","GLM","MAG","SEIS","SUVI","EXIS"],
            #required=False,
            #dest="instrument",
            help="GOES sensor/instrument making observations " + \
                    "(ie ABI, GLM, MAG, etc)"
            )
    parser.add_argument(
            #"-p",
            #"--process_level",
            "process_level",
            nargs="?",
            #default="L1b",
            default="-",
            choices=["-","L1b","L2"],
            #required=False,
            #dest="process_level",
            help="Preprocessing stage of the data product (ie L1b or L2)"
            )
    parser.add_argument(
            #"-d",
            #"--domain",
            "domain",
            nargs="?",
            #default="RadC",
            default="-",
            #choices=[],
            #required=False,
            #dest="domain",
            help="domain or scan sector (ie. RadC CONUS, RadM mesoscale)"
            )
    parser.add_argument(
            "-t",
            "--target_time",
            nargs="?",
            default=None,
            required=False,
            dest="target_time",
            help="Target for observations to retrieve. Serves as the " + \
                    "'anchor' point for describing a range with the " + \
                    "window_timedelta argument."
            )
    parser.add_argument(
            "-w",
            "--window_timedelta",
            nargs="?",
            default=-2,
            required=False,
            dest="window_timedelta",
            type=float,
            help="time window in hours"
            )
    parser.add_argument(
            "-s",
            "--substring",
            nargs="*",
            default=[],
            dest="substring",
            help="String or list of strings that must be contained in a " + \
                    "file in order for it to qualify for download"
            )
    parser.add_argument(
            "--animate",
            dest="animate",
            action="store_true",
            default=False,
            help="If set, download the entire selected range of files",
            )
    parser.add_argument(
            "-v",
            "--verbose",
            dest="quiet_files",
            action="store_false",
            default=True,
            help="If set, don't print all files returned by the initial search"
            )
    args = parser.parse_args()
    return args

if __name__=="__main__":
    data_dir = Path("/rstor/mdodson/goes/download")
    args = parse_args()
    if args.target_time is None:
        ttime = datetime.utcnow()
    else:
        ttime = datetime.strptime(args.target_time, "%Y%m%d%H%M")
    #wtime = ttime + timedelta(hours=args.window_timedelta)
    gs = search_goes(
            query=GOES_Product(
                satellite=None if args.goes_version=="-" \
                        else str(args.goes_version),
                sensor=None if args.instrument=="-" else args.instrument,
                level=None if args.process_level=="-" else args.process_level,
                scan=None if args.domain=="-" else args.domain,
                ),
            time=ttime,
            search_window=timedelta(hours=args.window_timedelta),
            label_substr=args.substring,
            quiet_files=args.quiet_files,
            )
    GG = GetGOES()
    if not len(gs):
        exit(0)
    if type(gs[0]) == GOES_File:
        unqt = list(set(f.stime for f in gs))
        _,tmin = sorted([(abs(t-ttime),t) for t in unqt], key=lambda v:v[0])[0]
        print(args.animate)
        if not args.animate:
            gs = list(filter(lambda f:f.stime==tmin, gs))
        resp = input(f"\nConfirm download {len(gs)} files (y/N): ")
        if resp.lower() != "y":
            exit(0)
    acquire_abi(gs, Path("/rstor/mdodson/goes/abi"))
