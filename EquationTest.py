import unittest
from task3 import equation

class TestEquation(unittest.TestCase):
    def test_equation_valid_args(self):
        # Test with valid input arguments
        self.assertEqual(equation(1, -3, 2), "x1 = 2.00 \nx2 = 1.00")

    def test_equation_zero_discr(self):
        # Test when discriminant is zero
        self.assertEqual(equation(1, -2, 1), "x = 1.00")

    def test_equation_no_roots(self):
        # Test when there are no roots
        self.assertEqual(equation(1, 2, 3), "Корней нет")

    def test_equation_invalid_args(self):
        # Test with invalid input arguments
        self.assertEqual(equation('a', 'b', 'c'), "Введите верные переменные")

if __name__ == '__main__':
    unittest.main()
