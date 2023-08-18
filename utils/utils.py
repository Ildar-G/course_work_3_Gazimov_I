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