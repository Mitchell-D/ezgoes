from pathlib import Path
from datetime import datetime,timedelta,UTC
from pprint import pprint

from GetGOES import GetGOES

tmp = {'C01': [{'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702001190_e20262702003564_c20262702003594.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 1, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702006190_e20262702008563_c20262702008587.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 6, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702011190_e20262702013563_c20262702013587.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 11, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702016190_e20262702018563_c20262702018585.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 16, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702021190_e20262702023563_c20262702023592.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 21, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702026190_e20262702028563_c20262702028585.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 26, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702031190_e20262702033563_c20262702033590.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 31, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702036190_e20262702038563_c20262702038589.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 36, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702041190_e20262702043563_c20262702043586.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 41, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702046190_e20262702048563_c20262702048590.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 46, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702051190_e20262702053563_c20262702053593.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 51, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C01_G18_s20262702056190_e20262702058564_c20262702058587.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 56, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702101190_e20262702103563_c20262702103591.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 1, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702106190_e20262702108563_c20262702108588.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 6, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702111190_e20262702113563_c20262702113591.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 11, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702116190_e20262702118563_c20262702118585.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 16, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702121190_e20262702123563_c20262702123591.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 21, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702126190_e20262702128563_c20262702128587.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 26, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702131190_e20262702133564_c20262702133594.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 31, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702136190_e20262702138564_c20262702138587.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 36, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702141190_e20262702143563_c20262702143587.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 41, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702146190_e20262702148564_c20262702148591.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 46, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702151190_e20262702153564_c20262702153585.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 51, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C01_G18_s20262702156190_e20262702158563_c20262702158586.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 56, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/22/OR_ABI-L1b-RadC-M6C01_G18_s20262702201190_e20262702203563_c20262702203589.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 22, 1, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/22/OR_ABI-L1b-RadC-M6C01_G18_s20262702206190_e20262702208564_c20262702208585.nc',
          'label': 'ABI-L1b-RadC-M6C01',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 22, 6, 19)}],
 'C02': [{'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702001190_e20262702003564_c20262702003585.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 1, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702006190_e20262702008563_c20262702008585.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 6, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702011190_e20262702013563_c20262702013583.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 11, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702016190_e20262702018563_c20262702018580.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 16, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702021190_e20262702023563_c20262702023585.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 21, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702026190_e20262702028563_c20262702028581.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 26, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702031190_e20262702033563_c20262702033581.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 31, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702036190_e20262702038563_c20262702038582.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 36, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702041190_e20262702043563_c20262702043583.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 41, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702046190_e20262702048563_c20262702048583.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 46, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702051190_e20262702053563_c20262702053582.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 51, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C02_G18_s20262702056190_e20262702058563_c20262702058583.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 56, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702101190_e20262702103563_c20262702103582.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 1, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702106190_e20262702108563_c20262702108584.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 6, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702111190_e20262702113563_c20262702113582.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 11, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702116190_e20262702118563_c20262702118581.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 16, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702121190_e20262702123563_c20262702123582.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 21, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702126190_e20262702128563_c20262702128583.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 26, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702131190_e20262702133563_c20262702133582.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 31, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702136190_e20262702138563_c20262702138583.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 36, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702141190_e20262702143563_c20262702143584.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 41, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702146190_e20262702148564_c20262702148582.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 46, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702151190_e20262702153563_c20262702153582.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 51, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C02_G18_s20262702156190_e20262702158563_c20262702158583.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 56, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/22/OR_ABI-L1b-RadC-M6C02_G18_s20262702201190_e20262702203563_c20262702203582.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 22, 1, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/22/OR_ABI-L1b-RadC-M6C02_G18_s20262702206190_e20262702208564_c20262702208582.nc',
          'label': 'ABI-L1b-RadC-M6C02',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 22, 6, 19)}],
 'C03': [{'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702001190_e20262702003564_c20262702003592.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 1, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702006190_e20262702008563_c20262702008591.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 6, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702011190_e20262702013564_c20262702013595.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 11, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702016190_e20262702018564_c20262702018591.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 16, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702021190_e20262702023563_c20262702023589.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 21, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702026190_e20262702028563_c20262702028589.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 26, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702031190_e20262702033563_c20262702033593.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 31, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702036190_e20262702038563_c20262702038586.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 36, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702041190_e20262702043563_c20262702043590.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 41, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702046190_e20262702048563_c20262702048586.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 46, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702051190_e20262702053564_c20262702053589.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 51, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/20/OR_ABI-L1b-RadC-M6C03_G18_s20262702056190_e20262702058564_c20262702058590.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 20, 56, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702101190_e20262702103564_c20262702103595.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 1, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702106190_e20262702108564_c20262702108593.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 6, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702111190_e20262702113563_c20262702113593.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 11, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702116190_e20262702118563_c20262702118587.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 16, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702121190_e20262702123563_c20262702123587.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 21, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702126190_e20262702128563_c20262702128590.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 26, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702131190_e20262702133564_c20262702133586.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 31, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702136190_e20262702138563_c20262702138590.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 36, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702141190_e20262702143563_c20262702143592.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 41, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702146190_e20262702148564_c20262702148588.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 46, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702151190_e20262702153564_c20262702153588.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 51, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/21/OR_ABI-L1b-RadC-M6C03_G18_s20262702156190_e20262702158563_c20262702158589.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 21, 56, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/22/OR_ABI-L1b-RadC-M6C03_G18_s20262702201190_e20262702203564_c20262702203592.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 22, 1, 19)},
         {'key': 'noaa-goes18/ABI-L1b-RadC/2026/270/22/OR_ABI-L1b-RadC-M6C03_G18_s20262702206190_e20262702208564_c20262702208589.nc',
          'label': 'ABI-L1b-RadC-M6C03',
          'product': ('18', 'ABI', 'L1b', 'RadC'),
          'stime': datetime(2026, 9, 27, 22, 6, 19)}]}

if __name__=="__main__":
    menu_path = Path("data/goes_product_menu.json")
    data_dir = Path("data/source")

    product = (18, "ABI", "L1b", "RadC")
    #end_time = datetime.now(UTC).replace(tzinfo=None)
    end_time = datetime(2026, 9, 27, 20)
    #start_time = end_time - timedelta(hours=2)
    start_time = datetime(2026, 9, 27, 17)
    channels = ["C01", "C02", "C03", "C04", "C07", "C13"]
    time_res_minutes = 10

    """ ------------( end normal configuration )------------ """

    gg = GetGOES(menu_file=menu_path, refetch=False)
    #'''
    sr = gg.search(
        product=product,
        start_time=start_time,
        end_time=end_time,
        substrings=channels,
        )
    #'''
    #sr = tmp

    ## make reference time steps in order to drop between time_res_minutes
    nt = int((end_time-start_time).total_seconds() // (60*time_res_minutes))
    target_times = [
        start_time + timedelta(minutes=i*time_res_minutes)
        for i in range(nt + 1)
        ]

    if isinstance(sr, list):
        sr = {"":sr}
    file_timeline = {}
    for ck,v in sr.items():
        tmpl = None
        tfiles = {}
        for f in v:
            ## make sure channels uniquely identify file labels so that
            ## channel labels can be used to id data types
            if tmpl is None:
                tmpl = f["label"]
            elif f["label"] != tmpl:
                raise ValueError(
                    "Substrings need to uniquely identify file labels.",
                    "{f['label']} != {tmpl}"
                    )
            ## find the closest in-range file for each target time step
            for t in target_times:
                tmp_dt = abs(t-f["stime"])
                if tmp_dt < timedelta(minutes=time_res_minutes / 2):
                    if not t in tfiles.keys() or tmp_dt < tfiles[t][0]:
                        tfiles[t] = [tmp_dt, f]

            ## associate matched timesteps with their files in chrono order
            get_files = []
            for t in target_times:
                get_files.append((t, tfiles.get(t, None)))

            ## set the most distant of redundant files to None rather than
            ## copying the same file multiple times.
            for i,(ta,a) in enumerate(get_files[:]):
                if a is None:
                    continue
                dta,fa = a
                for j,(tb,b) in enumerate(get_files[:]):
                    if b is None:
                        continue
                    dtb,fb = b
                    if i==j or fa["key"] != fb["key"]:
                        continue
                    if dta > dtb:
                        get_files[i][1] = None
                    else:
                        get_files[j][1] = None
            get_files = [
                [t, None if finfo is None else finfo[1]]
                for t,finfo in get_files
                ]
            #get_files = list(filter(lambda v:not v[1] is None, get_files))
            file_timeline[ck] = get_files

    import s3fs
    s3 = s3fs.S3FileSystem(anon=True)

    #pprint(file_timeline)
    for ck,fs in file_timeline.items():
        for t,finfo in fs:
            print(finfo)
            out_path = data_dir.joinpath(Path(finfo["key"]).name)
            s3.download(finfo["key"], out_path.as_posix())
            print([t, finfo, out_path.as_posix()])
