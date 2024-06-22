from datetime import datetime


def mask_account_card(input_string:str)->str:
    """Функция обрабатывает строку и если строка начинается со слова Счет
    по передает её для обработки в функцию mask_card с параметром в виде аргумента
    функции mask_account, если нет то в функцию mask_card(input_string)"""
    if input_string.startswith("Счет"):
        return mask_account(input_string)
    else:
        return mask_card(input_string)


def mask_card(card_info:str)->str:
    """Функция для преобразования номера счета"""
    card_type, card_number = card_info.split(maxsplit=1)
    masked_number = card_number[:4] + " **" + " **** " + card_number[-4:]
    return f"{card_type} {masked_number}"


def mask_account_card(account_info:str)->str:
    """Функция для преобразования номера карты"""
    account_number = account_info.split(maxsplit=1)
    masked_number = "**" + account_number[-4:]
    return f"Счет {masked_number}"


def get_data(input_date:str)->str:
    """Функция преобразования даты"""
    date_obj = datetime.strptime(input_date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_obj.strftime("%d.%m.%Y")
