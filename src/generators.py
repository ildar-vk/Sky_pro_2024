def filter_by_currency(transactions, currency):
    """Эта функция принимает список transactions и валюту currency.
      Она использует генераторное выражение для фильтрации транзакций по указанной валюте.
      Если переданный объект transactions является списком,
      то она перебирает каждую транзакцию в списке и,
      если валюта транзакции совпадает с указанной валютой,
      она возвращает эту транзакцию с помощью ключевого слова yield.
      В противном случае, если transactions не является списком,
      она также перебирает транзакции и возвращает соответствующие транзакции."""
    if isinstance(transactions, list):
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
    else:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions):
    '''
    Эта функция также использует генераторное выражение для перебора транзакций и
    возврата описания каждой транзакции с помощью yield.
    '''
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    '''
    Эта функция генерирует номера карт в заданном диапазоне.
    Она использует цикл for для создания номеров карт в заданном диапазоне и
    возвращает их с помощью yield.
    '''
    for num in range(start, end + 1):
        yield "{:04d} {:04d} {:04d} {:04d}".format(
            (num // 10**12) % 10**4, (num // 10**8) % 10**4, (num // 10**4) % 10**4, num % 10**4
        )
