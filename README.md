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

If you just want to download some GOES data quickly, clone the
repository, then modify the `test_goes_download.py` script according
to the comments inside.

By default, this script will download the last 30 minutes of GOES-16
ABI channel 13 data if you set the `data_dir` variable to an
existing directory, but you can download any GOES product within a
specified time range by modifiying the arguments in the file.

If you aren't sure which product you want, you can search for valid
product labels by only providing a partial `GOES_Product` object. In
the following example, the scan attribute is left out, so the method
will return all valid L2 products for GOES ABI.

```python
search_goes(GOES_Product(satellite="18",sensor="ABI",level="L2"))
```

Alternatively, if you want to use this module in your code, copy
the _inner_ directory `ezgoes` (containing `__init__.py`) into the
same directory as your code, then import the methods or objects you
need in the same way `test_goes_download.py` does.

## minimal example

If the ezgoes module is in the current directory, this program will
download the most recent band 13 radiances over CONUS to the current
directory.

```python
from datetime import datetime
from pathlib import Path
from ezgoes import GetGOES, GOES_Product

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
```

## object types

In case you're interested in using this module in your own code,
`GetGOES`, `GOES_Product`, and `GOES_File` are the main 3 objects to
familiarize yourself with. `TextFormat` is just a helper class for
formatting the terminal text printing style. with
[ansi escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code).

### GetGOES

The `GetGOES` object provides access to the GOES S3 bucket API,
enabling the user to:

 - Search for valid products given constraints with
   `GetGOES.search_products`
 - Identify available files with `GetGOES.search_hour`,
   `GetGOES.search_range`, or `GetGOES.search_closest_to_time`.
 - Download single files with `GetGOES.download`

See the internal documentation for more details.

### GOES\_Product

The `GOES_Product` object is a namedtuple that identifies a specific
bucket directory with a combination of satellite, sensor, level, and
scan properties.

 - __satellite__: GOES generation; one of ("16", "17", "18")
 - __sensor__: GOES satellite sensor; one of:
   ("MAG", "SEIS", "SUVI", "EXIS", "GLM", "ABI")
 - __level__: Data processing level; one of ("L1b", "L2")
 - __scan__: Satellite scan or data type. Use `visual_search` or
  `GetGOES.search_products` to see options, or read the
  [NOAA bucket documentation][2]

[2]: https://github.com/awslabs/open-data-docs/tree/main/docs/noaa/noaa-goes16

By default, a `GOES_Product` object has its fields set to None.

### GOES\_File

The `GOES_File` is a namedtuple that identifies a specific file
available on the bucket with its product, stime, label, and path
properties.

 - __product__: `GOES_Product` describing the file's product type.
 - __stime__: `datetime` object depicting the start time of this
   file, which is the fourth underscore-separated field in the name.
 - __label__: Second underscore-separated field in the file name,
   which specifies the sub-product type of the file. For example,
   ABI L2 band 13 brightness temperatures have the label
   `ABI-L2-CMIPC-M6C13`.
 - __path__: AWS bucket path to the provided file.
