import h5py
import numpy as np
from pathlib import Path
from datetime import datetime,timedelta
from multiprocessing import Pool

from ezgoes import GOES_File,GOES_Product,GetGOES

def _gdl(args):
    new_path = GetGOES().download(*args)

def acquire_abi(abi_files:list, dest_dir:Path, buf_dir:Path=None, workers=4):
    """
    """
    products = list(set(tuple(f.label.split("-")[:3]) for f in abi_files))
    assert len(products)==1,f"Only 1 product type allowed ({products})"
    times = sorted(list(set(f.stime for f in abi_files)))
    feats = sorted(list(set(
        "-".join(tuple(f.label.split("-")[3:])) for f in abi_files
        )))
    with Pool(workers) as pool:
        for pool.

    print(times)
    print(feats)
