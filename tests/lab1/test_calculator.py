import unittest

from src.lab1.calculator import calculate, divide, parse_number, power, square_root


class CalculatorTestCase(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculate("+", 2, 3), 5)
        self.assertEqual(calculate("-", 2, 3), -1)
        self.assertEqual(calculate("*", 4, 2.5), 10.0)
        self.assertEqual(calculate("/", 7, 2), 3.5)

    def test_power_and_sqrt(self):
        self.assertEqual(power(2, 10), 1024)
        self.assertEqual(calculate("^", 9, 0.5), 3.0)
        self.assertEqual(square_root(25), 5.0)

    def test_errors(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)
        with self.assertRaises(ValueError):
            square_root(-1)
        with self.assertRaises(ValueError):
            calculate("%", 1, 2)
        with self.assertRaises(ValueError):
            calculate("+", 1)

    def test_parse_number(self):
        self.assertEqual(parse_number(" 42 "), 42)
        self.assertEqual(parse_number("3,5"), 3.5)
        with self.assertRaises(ValueError):
            parse_number("abc")
