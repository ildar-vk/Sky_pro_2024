def filter_by_state(data, state="EXECUTED"):
    """

    :param data: в функцию в виде аргумента подается список словарей
    :param state: по умолчанию 'EXECUTED' возвращает новый список, содержащий только те словари, у которых ключ
                state
                содержит переданное в функцию значение.
    """
    return [d for d in data if d.get("state") == state]


def sort_by_date(data, reverse=True):
    """

    :param data: в функцию в виде аргумента подается список словарей
    :param reverse: второй необязательный задает порядок сортировки (убывание, возрастание).
    """
    return sorted(data, key=lambda x: x["date"], reverse=reverse)

