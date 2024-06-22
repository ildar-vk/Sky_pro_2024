import pytest

import src.widget


def test_mask_account_card():
    input_data = [
        ("Maestro 1596837868705199", "Maestro 1596 ** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 ** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Clas ** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Plat ** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold ** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ]
    for data, expected_output in input_data:
        assert src.widget.mask_account_card(data) == expected_output


@pytest.mark.parametrize(
    "kard_accaunt,ghost_kard_accaunt",
    [
        ("Maestro 1596837868705199", "Maestro 1596 ** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 ** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Clas ** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Plat ** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold ** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_param(kard_accaunt, ghost_kard_accaunt):
    assert src.widget.mask_account_card(kard_accaunt)


def test_et_data_Out_date(Out_date):
    assert src.widget.get_data("2018-07-11T02:26:18.671407") == Out_date
