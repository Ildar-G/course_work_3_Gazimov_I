import json
import pytest
from utils.utils import load_operations, sort_list, get_executed, date_format, mask_card


def test_load_operations():
    assert list == type(load_operations('../operations.json'))
