def get_mask_card_number(card_number:str)->str:
    visible_digits = 6
    masked_number = (
        card_number[:visible_digits]
        + " "
        + " ".join(
            ["**" if i < visible_digits + 2 else "****" for i in range(visible_digits, len(card_number) - 4, 4)]
        )
        + " "
        + card_number[-4:]
    )
    return masked_number


def get_mask_account(account_number:str)->str:
    visible_digits = 4
    masked_number = "**" + account_number[-visible_digits:]
    return masked_number



