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