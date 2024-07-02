import pytest

import src.decorators


def test_for_Exception():
    with pytest.raises(Exception):
         @src.decorators.log("log.txt")
         def add(a, b):
            return a / b

         print(add(2,0))



def test_log():
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5


#