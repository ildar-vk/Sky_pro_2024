def currency_filter(currency):
    def decorator(func):
        def wrapper(transactions):
            for transaction in func(transactions):
                if transaction["operationAmount"]["currency"]["code"] == currency:
                    yield transaction

        return wrapper

    return decorator


@currency_filter("USD")
def filter_by_currency(transactions):
    for transaction in transactions:
        yield transaction


def transaction_descriptions(transactions):
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, end):
    for num in range(start, end + 1):
        yield "{:04d} {:04d} {:04d} {:04d}".format(
            (num // 10**12) % 10**4, (num // 10**8) % 10**4, (num // 10**4) % 10**4, num % 10**4
        )
