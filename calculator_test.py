from calculator import Calculator


calc = Calculator()

def test_add_method():
    assert calc.add(0, 1) == 1
    assert Calculator.add(1, 0) == 1
    assert Calculator.add(0, 2) == 2
    assert Calculator.add(2, 0) == 2
    assert Calculator.add(1, 1) == 2
    assert Calculator.add(1, 2) == 3
    assert Calculator.add(2, 1) == 3

def test_subtract_method():
    assert Calculator.subtract (0, 1) == -1
    assert Calculator.subtract (0, 2) == -2
    assert Calculator.subtract (1, 0) == 1
    assert Calculator.subtract (2, 0) == 2
    assert Calculator.subtract (2, 1) == 0
