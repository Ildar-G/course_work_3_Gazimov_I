import json
import pytest
from utils.utils import load_operations, sort_list, get_executed, date_format, mask_card


def test_load_operations():
    assert list == type(load_operations('../operations.json'))


def test_sort_list():
    test_list = [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364"
        }
    ]

    assert sort_list(test_list) == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        }
    ]