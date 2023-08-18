import json
import datetime

def load_operations(filename):
    """
    Функция принимает в качестве аргумента строку из файла operations json
    и возвращает список словарей
    """
    with open(filename, "r", encoding="UTF-8") as file:
        list_ = json.load(file)
    return list_


def date_format(date):
    """
    Функция принимает строку с датой в формате "2019-08-26T10:50:58.294041"
    и возвращет в формате 26.08.2019
       """
    str_date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    formated_date = str_date.strftime('%d.%m.%Y')
    return formated_date


def sort_list(operations):
    """
    Функция cортирует список словарей по дате
    и возвращает отсортированный список.
        """
    operations.sort(key=lambda x: x.get('date'), reverse=True)
    return operations


def get_executed(operations):
    """
    Функция принимсает список словарей
    фильтрует по состоянию EXECUTED и возвращает отфильтрованный список
       """
    executed_list = []
    for item in operations:
        if item.get('state') == 'EXECUTED':
            executed_list.append(item)
    return executed_list


def mask_card(card):
    """
    Функция принимает строку и скрывает элементы по маске
    """
    if not card:
        return ''
    card_data = card.split(' ')
    if card_data[0] == 'Счет':
        return card_data[0] + '**' + card_data[1][-4:]
    card_number = card_data[-1][:4] + ' ' + card_data[-1][4:6] + '** **** ' + card_data[-1][-4:]
    return ' '.join(card_data[:-1]) + ' ' + card_number