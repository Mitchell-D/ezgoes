"""
Straightforward module for searching for and downloading GOES data from the
NOAA S3 bucket on AWS.
"""
from .get_goes import GetGOES, search_goes
from .goes_info import GOES_Product, GOES_File
from .goes_info import goes_descriptions, goes_products
from .TextFormat import TextFormat

