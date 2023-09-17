# simple_calculator.py

import math
import re


def greet_user():
    print("Welcome to the console calculator")


def show_instructions():
    print("Please enter two digits and an operation (+, -, *, /).")
    print("Separate your input by spaces. For example, you can enter: 10 + 5")


def validate_format(user_input):
    parts = user_input.split()

    if len(parts) == 1:
        # Remove whitespaces and then check if the input contains two numbers and an operator
        input_without_spaces = ''.join(user_input.split())

        # Ensure the input consists of digits, followed by one of the operators (+, -, *, /),
        # followed by more digits.
        if not re.match(r'^-?[0-9.]+ ?[+\-*/] ?-?[0-9.]+$', input_without_spaces):
            print(f"Invalid input. Please follow the format: <num1> <operator> <num2>.")
            return True
        else:
            return None

    elif len(parts) == 2:
        print(f"Invalid input. Please follow the format: <num1> <operator> <num2>.")
        return True

    elif len(parts) > 3:
        print(f"Invalid input. Please follow the format: <num1> <operator> <num2>.")
        return True


def validate_input(user_input):

    try:
        input_without_spaces = ''.join(user_input.split())
        num1 = ''
        num2 = ''
        operator = ''

        i = 0
        while i < len(input_without_spaces):
            char = input_without_spaces[i]

            # Handle the first character as a potential negative sign
            if char == '-' and i == 0:
                num1 += '-'
                i += 1
                continue

            if char == '-' and i != 0:
                num2 += '-'
                i += 1
                continue

            # Check if the character is a digit or a decimal point
            if char.isdigit() or char == '.':
                if operator == '':
                    num1 += char
                else:
                    num2 += char
                i += 1
            elif operator == '':
                operator = char
                i += 1
            else:
                return None, None, None, f"INVALID: You need to enter a number!"

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
