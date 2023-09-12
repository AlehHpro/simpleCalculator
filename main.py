# simpleCalculator.py

import math
import re


def greet_user():
    print("Welcome to the console calculator")


def show_instructions():
    print("Please enter two digits and an operation (+, -, *, /).")
    print("Separate your input by spaces. For example, you can enter: 10 + 5")


def validate_format(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print(f"Invalid input. Please follow the format: <num1> <operator> <num2>.")
        return True
    else:
        return None


def validate_input(user_input):

    # Possible input check with RegEx:
    # Check if input contains only digits, decimal points, operator, and whitespace
    # if not re.match(r'^[0-9+.\-*/\s]+$', user_input):
    #     return None, "Invalid characters in input. Please use digits, operators (+, -, *, /), and spaces only."

    try:
        num1, operator, num2 = user_input.split()

        # Replace any comma (,) with a period (.) for decimal numbers
        num1 = num1.replace(',', '.')
        num2 = num2.replace(',', '.')

        try:
            num1 = float(num1)
        except ValueError:
            return None, operator, num2, "INVALID: You need to enter a number!"
        try:
            num2 = float(num2)
        except ValueError:
            return num1, operator, None, "INVALID: You need to enter a number!"

        if operator not in ['+', '-', '*', '/']:
            return num1, num2, None, "Invalid operator. Please use +, -, *, /."

        return num1, operator, num2, None
    except Exception as e:
        return None, f"An unexpected error occurred: {str(e)}"


def calculate_result(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return None, "Division by zero is not allowed."
        result = num1 / num2
    else:
        raise Exception(f"An unexpected error occurred!")
    return round(result, 3), None


def main():
    greet_user()
    show_instructions()

    while True:
        user_input = input("Enter your calculation (or 'quit' to exit): ").strip().lower()

        if user_input == 'quit':
            print("Goodbye!")
            break

        if validate_format(user_input):
            continue

        num1, operator, num2, validation_message = validate_input(user_input)

        if validation_message:
            print(f"Validation Error: {validation_message}")
            continue

        result, validation_message = calculate_result(num1, operator, num2)

        if validation_message:
            print(f"Validation Error: {validation_message}")
        else:
            print(f"Result: {result}")


if __name__ == "__main__":
    main()
