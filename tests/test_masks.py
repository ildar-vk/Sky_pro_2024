import pytest

import src.masks


def test_get_mask_card_number_Ghost_card(Ghost_card):
    assert src.masks.get_mask_card_number("7000792289606361") == Ghost_card

def test_get_mask_account_Ghost_card_account(Ghost_card_account):
    assert src.masks.get_mask_account('7000792289606361') == Ghost_card_account

# def test_mask_number_length():
#     assert src.masks.get_mask_card_number("12345678901234567890") == "123456 ****** 7890"
#     assert src.masks.get_mask_card_number("98765") == "98765"
#
# def test_mask_number_invalid_input():
#     assert src.masks.get_mask_card_number("") is None
#     assert src.masks.get_mask_card_number("12345a6789012345") is None


