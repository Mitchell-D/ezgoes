# ezgoes

Straightforward script for searching for and downloading GOES data
from the NOAA S3 bucket on AWS.

## dependency

The only dependency that isn't default on most environment managers
is [s3fs][1], which is a PyPI package that wraps the boto interface
and makes it much easier to use.

You can install s3fs with pip, or with conda using conda-forge

 1. `pip install s3fs`
 2. `conda install s3fs -c conda-forge`

[1]: https://s3fs.readthedocs.io/en/latest/

## how to use

In order to search for or download any GOES product, the only script
you need to execute is `get_goes.py`. Please see the bottom of that
file in the `__name__=="__main__"` section for detailed comments.

By default, this script will download the last 30 minutes of GOES-16
ABI channel 13 data if you set the `data_dir` variable to an
existing directory.

You can narrow down valid options using the `search_goes()` method.
For example, calling `search_goes(GOES_)`

## object types

### GetGOES

The `GetGOES` object provides access to the GOES S3 bucket API,
enabling the user to:

 - Search for valid products given constraints with
   `GetGOES.search_products`
 - Identify available files with `GetGOES.search_hour`,
   `GetGOES.search_range`, or `GetGOES.search_closest_to_time`.
 - Download single files with `GetGOES.download()`

### GOES\_Product

The `GOES_Product` object is a namedtuple that identifies a specific
bucket directory with a combination of satellite, sensor, level, and
scan properties.

 - _satellite_: GOES generation; one of ("16", "17", "18")
 - _sensor_: GOES satellite sensor; one of:
   ('MAG', 'SEIS', 'SUVI', 'EXIS', 'GLM', 'ABI')
 - _level_: Data processing level; one of ("L1b", "L2")
 - _scan_: Satellite scan or data type. Use `visual_search` or
  `GetGOES.search_products` to see options, or read the
  [NOAA bucket documentation][2]

[2]: https://github.com/awslabs/open-data-docs/tree/main/docs/noaa/noaa-goes16

By default, a `GOES_Product` object has its fields set to None.

### GOES\_File

The `GOES_File` object identifies a specific file available on the
bucket with product, stime, label, and path properties.

 - _product_: `GOES_Project` object describing this file's type.
 - _stime_: `datetime` object depicting the start time of this file,
   which is the fourth underscore-separated field in the file name.
 - _label_: Second underscore-separated field in the file name, which
   specifies the sub-product type of the file. For example, ABI L2
   band 13 brightness temperatures have label `ABI-L2-CMIPC-M6C13`.
 - _path_: AWS bucket path to the provided file.
