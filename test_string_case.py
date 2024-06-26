
from unittest import TestCase
from string_calculator import add

class TestStringCalculator(TestCase):
    def test_no_number_sum(self):
        self.assertEqual(add(""), 0)

    def test_one_number_sum(self):
        self.assertEqual(add("1"), 1)

    def test_two_number_sum(self):
        self.assertEqual(add("1, 2, 4"), 7)
    
    def test_sum_with_newline(self):
        self.assertEqual(add("1 \n 2, 4"), 7)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n 1; 2"), 3)
    
    def test_negative_numbers(self):
        self.assertRaises(ValueError, add, "-1")
        