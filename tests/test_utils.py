import json
import pytest
from utils.functions import load_operations, sort_list, get_executed, date_format, mask_card
from main import main, FILENAME


def test_load_operations():
    assert type(load_operations(operations.json) == list