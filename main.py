FILENAME = 'operations.json'
from utils.utils import load_operations, get_executed, sort_list, date_format, mask_card


def main(file):
    operations = load_operations(file) #получение данных из файла operations.json'
    executed = get_executed(operations) #список отсортированных по признаку 'EXECUTED' транзакций
    sorted_operations = sort_list(executed) #сортировка по дате
    last_five = sorted_operations[:5] #пять последних транзакций
    for item in last_five:
        date = date_format(item.get('date'))
        description = item.get('description')
        from_ = mask_card(item.get('from'))
        to_ = mask_card(item.get('to'))
        amount = item.get('operationAmount').get('amount')
        currency = item.get('operationAmount').get('currency').get('name')
        if from_:
            from_ = from_ + ' -> '
        print(f"{date} {description}\n"
              f"{from_}{to_}\n"
              f"{amount} {currency}\n")
    return last_five[-1:]


if __name__ == "__main__":
    main(FILENAME)