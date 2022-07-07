from cli_imagefetcher.cli import requestArguments
from cli_imagefetcher.validation import _payloadValidate
from .CONSTANTS import *
import pytest, os

BASIC_TEST = TEST_CONFIGURATIONS["basic"]


def test_payload():
    apikey = BASIC_TEST["apikey"]
    toi = BASIC_TEST["aoi"]
    aoi = _largeString()
    with pytest.raises(Exception) as e_info:
        _payloadValidate(apikey, toi, aoi)


def _largeString():
    # make translation table from 0..255 to 97..122
    tbl = bytes.maketrans(
        bytearray(range(256)),
        bytearray([ord(b"a") + b % 26 for b in range(256)]),
    )
    # generate random bytes and translate them to lowercase ascii
    return os.urandom(1000000).translate(tbl)
