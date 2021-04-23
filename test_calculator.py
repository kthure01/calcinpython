from calculator import Calculator


def test_add():
    assert 4 == Calculator.add(2, 2)
    assert 4 == Calculator.add(2, 3)
    assert Calculator.add(2, 3) == 5
