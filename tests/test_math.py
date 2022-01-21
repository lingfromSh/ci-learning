from src.math import plus
from ward import test


@test("Plus returns a + b.")
def test_plus():
    assert plus(0, 1) == 1, "0 + 1 == 1"
    assert plus(1, 1) == 2, "1 + 1 == 2"
    assert plus(2, 1) == 3, "2 + 1 == 3"
    assert plus(3, 1) == 4, "3 + 1 == 4"
    assert plus(4, 1) == 5, "4 + 1 == 5"
    assert plus(5, 1) == 6, "5 + 1 == 6"
    assert plus(6, 1) == 7, "6 + 1 == 7"
    assert plus(7, 1) == 8, "7 + 1 == 8"
    assert plus(8, 1) == 9, "8 + 1 == 9"
    assert plus(9, 1) == 10, "9 + 1 == 10"
