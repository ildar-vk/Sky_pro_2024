def currency_filter(currency):
    def decorator(func):
        def wrapper(transactions):
            for transaction in func(transactions):
                if transaction["operationAmount"]["currency"]["code"] == currency:
                    yield transaction
        return wrapper
    return decorator

# Функция, которую мы будем тестировать
@currency_filter("USD")
def filter_by_currency(transactions):
    for transaction in transactions:
        yield transaction

# Тестирование декоратора
def test_currency_filter():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}, "amount": 100}},
        {"operationAmount": {"currency": {"code": "EUR"}, "amount": 50}},
        {"operationAmount": {"currency": {"code": "USD"}, "amount": 75}}
    ]
    
    filtered_transactions = list(filter_by_currency(transactions))
    
    # Проверяем, что остались только транзакции с валютой USD
    assert len(filtered_transactions) == 2
    # Проверяем суммы транзакций
    assert filtered_transactions[0]["operationAmount"]["amount"] == 100
    assert filtered_transactions[1]["operationAmount"]["amount"] == 75