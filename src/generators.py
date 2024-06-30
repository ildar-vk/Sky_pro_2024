def filter_by_currency(transactions, currency):
    if isinstance(transactions, list):
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
    else:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    for num in range(start, end + 1):
        yield "{:04d} {:04d} {:04d} {:04d}".format(
            (num // 10**12) % 10**4, (num // 10**8) % 10**4, (num // 10**4) % 10**4, num % 10**4
        )
