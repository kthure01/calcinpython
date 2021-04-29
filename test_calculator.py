from calculator import Calculator


class TestCalculator:
    def test_add(self):
        assert 5 == Calculator.add(2, 2)
