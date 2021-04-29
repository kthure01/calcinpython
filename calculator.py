class Calculator:
    def __init__(self):
        pass  # Empty

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return 0

        return x / y


# calc = Calculator()

# print(calc.add(5, 5))
