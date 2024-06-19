#  Пример работы функции, возвращающей маску карты
# 7000792289606361     # входной аргумент
# 7000 79** **** 6361  # выход функции
#
# Пример работы функции, возвращающей маску счета
# 73654108430135874305  # входной аргумент
# **4305  # выход функции

import pytest



def test_get_mask_card_number(Ghost_card):
    assert Ghost_card == ['7000 79** **** 6361']

def test_get_mask_account(Ghost_card_account):
    assert Ghost_card_account ==['**4305']



