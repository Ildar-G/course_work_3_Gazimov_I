import json
import pytest
from utils.utils import load_operations, sort_list, get_executed, date_format, mask_card
from main import main

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

def test_date_format():
    assert date_format("2018-09-12T21:27:25.241689") == "12.09.2018"
    assert date_format("2019-07-03T18:35:29.512364") == "03.07.2019"


def test_get_executed():
    test_list = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
        }

    ]
    assert get_executed(test_list) == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
        },
    ]

@pytest.mark.parametrize('str_card, mask', [('Счет 44812258784861134719', 'Счет**4719'),
                                            ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                            (None, '')])
def test_mask_card(str_card, mask):
    assert mask_card(str_card) == mask


def test_main():
    assert main("../operations.json") == [{
        'date': '2019-11-05T12:04:13.781725',
        'description': 'Открытие вклада',
        'id': 801684332,
        'operationAmount': {
            'amount': '21344.35',
            'currency': {
                'code': 'RUB',
                'name': 'руб.'
            }
        },
        'state': 'EXECUTED',
        'to': 'Счет 77613226829885488381'
    }
    ]