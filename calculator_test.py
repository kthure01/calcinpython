from calculator import Calculator


calc = Calculator()

def test_add_method():
    assert calc.add(0, 1) == 1
    assert 1 == Calculator.add(1, 0)
    assert 2 == Calculator.add(0, 2)
    assert 2 == Calculator.add(2, 0)
    assert 2 == Calculator.add(1, 1)
    assert 3 == Calculator.add(1, 2)
    assert 3 == Calculator.add(2, 1)


def test_subtract_method():
    assert -1 == Calculator.subtract (0, 1)
    assert -2 == Calculator.subtract (0, 2)
    assert 1 == Calculator.subtract (1, 0)
    assert 2 == Calculator.subtract (2, 0)
    assert 0 == Calculator.subtract (2, 1)
