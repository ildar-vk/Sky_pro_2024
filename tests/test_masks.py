#  Пример работы функции, возвращающей маску карты
# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции
#
# Пример работы функции, возвращающей маску счета
# 73654108430135874305  # входной аргумент
# **4305  # выход функции

import pytest

def test_get_mask_card_number_Ghost_card(Ghost_card):
    assert  '7000792289606361'== Ghost_card

def test_get_mask_account_Ghost_card_account(Ghost_card_account):
    assert '73654108430135874305' == Ghost_card_account



