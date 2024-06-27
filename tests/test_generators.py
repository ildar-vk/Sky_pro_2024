from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency():
    transactions = [
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 1"},
        {"operationAmount": {"currency": {"code": "EUR"}}, "description": "Transaction 2"},
        {"operationAmount": {"currency": {"code": "USD"}}, "description": "Transaction 3"}
    ]
    filtered_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(filtered_transactions) == 2
    assert filtered_transactions[0]["description"] == "Transaction 1"
    assert filtered_transactions[1]["description"] == "Transaction 3"

def test_transaction_descriptions():
    transactions = [
        {"description": "Transaction 1"},
        {"description": "Transaction 2"},
        {"description": "Transaction 3"},
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == 3
    assert descriptions == ["Transaction 1", "Transaction 2", "Transaction 3"]

def test_card_number_generator():
    card_numbers = list(card_number_generator(1234567890123456, 1234567890123460))
    assert len(card_numbers) == 5
    assert card_numbers == [
        "1234 5678 9012 3456",
        "1234 5678 9012 3457",
        "1234 5678 9012 3458",
        "1234 5678 9012 3459",
        "1234 5678 9012 3460",
    ]