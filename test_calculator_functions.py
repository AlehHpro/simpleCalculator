import sys
import unittest
from io import StringIO

from simple_calculator import greet_user, show_instructions, validate_input, calculate_result, validate_format


class TestCalculatorFunctions(unittest.TestCase):
    def test_greet_user(self):
        self.assertIsNone(greet_user())  # Check if the function returns None

    def test_show_instructions(self):
        self.assertIsNone(show_instructions())  # Check if the function returns None

    def test_validate_input_valid(self):
        num1, operator, num2, validation_message = validate_input("10 + 5")
        self.assertEqual((num1, operator, num2, validation_message), (10, '+', 5.0, None))

    def test_validate_input_invalid_operator(self):
        _, _, _, validation_message = validate_input("10 % 5")
        self.assertEqual(validation_message, "Invalid operator. Please use +, -, *, /.")

    def test_validate_input_invalid_number(self):
        _, _, _, validation_message = validate_input("10 + abc")
        self.assertEqual(validation_message, "INVALID: You need to enter a number!")

    def test_calculate_result_addition(self):
        result, validation_message = calculate_result(10.0, '+', 5.0)
        self.assertEqual((result, validation_message), (15.0, None))

    def test_calculate_result_subtraction(self):
        result, validation_message = calculate_result(10.0, '-', 5.0)
        self.assertEqual((result, validation_message), (5.0, None))

    def test_calculate_result_multiplication(self):
        result, validation_message = calculate_result(10.0, '*', 5)
        self.assertEqual((result, validation_message), (50.0, None))

    def test_calculate_result_division(self):
        result, validation_message = calculate_result(10.0, '/', 5.0)
        self.assertEqual((result, validation_message), (2.0, None))

    def test_calculate_result_division_by_zero(self):
        _, validation_message = calculate_result(10.0, '/', 0.0)
        self.assertEqual(validation_message, "Division by zero is not allowed.")

# Tests for def validate_format(user_input):
    def setUp(self):
        # Redirect sys.stdout to capture print statements
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        # Reset sys.stdout to its original state
        sys.stdout = self.original_stdout

    def test_valid_input(self):
        # Test a valid input with three parts
        result = validate_format("10 + 5")
        self.assertIsNone(result)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_invalid_input_too_few_parts(self):
        # Test an invalid input with too few parts
        result = validate_format("10 +")
        self.assertTrue(result)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Invalid input. Please follow the format: <num1> <operator> <num2>.")

    def test_invalid_input_too_many_parts(self):
        # Test an invalid input with too many parts
        result = validate_format("10 + 5 3")
        self.assertTrue(result)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Invalid input. Please follow the format: <num1> <operator> <num2>.")


if __name__ == '__main__':
    unittest.main()
