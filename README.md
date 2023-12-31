# Console Calculator

This is a simple console calculator application written in Python 3.
It allows you to perform basic arithmetic operations.

## Requirements

- Python 3

## How to Use

1. **Clone the repository:**

git clone https://github.com/AlehHpro/simpleCalculator.git

2. **Navigate to the project directory:**

cd simpleCalculator

3. **Run the calculator:**

python simple_calculator.py

4. **Follow the instructions:**

- Upon running the calculator, you will be greeted and given instructions.
- Enter your calculations in the format `<num1> <operator> <num2>`, for example, `10 + 5`.
- The result will be displayed rounded to 3 decimal places.
- To exit the calculator, simply type `quit`.

## Running Unit Tests

1. Open your terminal.

2. Navigate to the directory where your Python project is located using the `cd` command. For example:

   ```bash
   cd /path/to/your/python/project

- Run the following command to execute your unit tests:

  python -m unittest test_calculator_functions

- Replace test_calculator_functions with the name of the Python file containing your test cases.
  This file should be in the same directory as your main code or within a tests directory,
  depending on your project structure.

  For example, if your test cases are in a file named test_calculator_functions.py, you would run:

  python -m unittest test_calculator_functions

- The tests will run, and you'll see the output in the terminal.
  Successful tests will be indicated by dots (.), and any failed tests will display an 'F' character
  along with a summary of the failures.

.....
----------------------------------------------------------------------
Ran 5 tests in 0.123s

OK

- If there are any test failures, the output will provide details about which tests failed and why.
