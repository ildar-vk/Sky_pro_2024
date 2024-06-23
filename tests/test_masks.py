import src.masks


def test_get_mask_card_number_Ghost_card(Ghost_card):
    assert src.masks.get_mask_card_number("7000792289606361") == Ghost_card


def test_get_mask_account_Ghost_card_account(Ghost_card_account):
    assert src.masks.get_mask_account("7000792289606361") == Ghost_card_account
