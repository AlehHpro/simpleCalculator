import unittest

from main import greet_user, show_instructions, validate_input, calculate_result


class TestCalculatorFunctions(unittest.TestCase):
    def test_greet_user(self):
        self.assertIsNone(greet_user())  # Check if the function returns None

    def test_show_instructions(self):
        self.assertIsNone(show_instructions()) # Check if the function returns None

    def test_validate_input_valid(self):
        num1, operator, num2, validation_message = validate_input("10 + 5")
        self.assertEqual((num1, operator, num2, validation_message), (10, '+', 5.0, None))


if __name__ == '__main__':
    unittest.main()
