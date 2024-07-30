import os
from src.utils import input_data
from src.utils import filter_transactions_by_description


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input("Ваш выбор: ")

        if choice == '1':
            file_path = os.path.join('data', 'transactions1.json')
            transactions = input_data(file_path)
        elif choice == '2':
            file_path = os.path.join('data', 'transactions.csv')
            transactions = input_data(file_path)
        elif choice == '3':
            file_path = os.path.join('data', 'transactions.xlsx')
            transactions = input_data(file_path)
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
            continue

        while True:
            status = input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
                "Ваш статус: "
            ).strip().upper()

            if status in {'EXECUTED', 'CANCELED', 'PENDING'}:
                print(f"Операции отфильтрованы по статусу '{status}'.")
                filtered_transactions = [t for t in transactions if t['status'].upper() == status]
                break
            else:
                print(f'Статус операции "{status}" недоступен.')

        sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
        if sort_choice == 'да':
            order_choice = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
            reverse = order_choice == 'по убыванию'
            filtered_transactions.sort(key=lambda x: x['date'], reverse=reverse)

        currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
        if currency_choice == 'да':
            filtered_transactions = [t for t in filtered_transactions if t['currency'] == 'RUB']

        word_filter_choice = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
        ).strip().lower()

        if word_filter_choice == 'да':
            search_string = input("Введите слово для поиска: ")
            filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

        print("Распечатываю итоговый список транзакций...")

        if not filtered_transactions:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        else:
            print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
            for transaction in filtered_transactions:
                print(
                    f"{transaction['date']} {transaction['description']}\n"
                    f"Счет **{transaction['account']}\n"
                    f"Сумма: {transaction['amount']} {transaction['currency']}\n"
                )


if __name__ == "__main__":
   main()