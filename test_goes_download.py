from datetime import datetime, timedelta
from pathlib import Path
from ezgoes import search_goes, GetGOES, GOES_Product
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
