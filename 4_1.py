import unittest

class FactorialCalculator:
    def __init__(self):
        self.factorials = []

    def calculate_factorials(self, n):
        if n < 0:
            raise ValueError("n must be above 0")

        self.factorials = [self._calculate_factorial(i) for i in range(n)]

    def get_factorials(self):
        print(self.factorials)
        return self.factorials

    def _calculate_factorial(self, num):
        if num == 0:
            return 1
        if num < 0:
            raise ValueError("Factorial is defined only for\
                              non-negative numbers")
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

class TestFactorialCalculator(unittest.TestCase):
    def test_calculate_factorials(self):
        calculator = FactorialCalculator()
        calculator.calculate_factorials(5)
        self.assertEqual(calculator.get_factorials(), [1, 1, 2, 6, 24])

    def test_negative_input(self):
        calculator = FactorialCalculator()
        with self.assertRaises(ValueError):
            calculator.calculate_factorials(-3)

if __name__ == "__main__":
    unittest.main()