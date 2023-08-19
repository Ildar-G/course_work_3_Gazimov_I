from main import main


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
