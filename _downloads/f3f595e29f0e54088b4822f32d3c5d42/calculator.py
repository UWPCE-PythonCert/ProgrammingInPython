#!/usr/bin/env python3

"""calculator

    Usage:

    calculator.py 1 + 3

"""

import sys

import calculator_functions as functions


# put the real code in a function so we can test it
def main():

    if len(sys.argv) != 4:
        error_message = """

            Invalid arguments.

            Usage:

            calculator.py 1 + 3

            or 1 x 3
            or 1 / 3
            or 1 - 3
            """
        raise ValueError(error_message + "\n")

    x = sys.argv[1]
    operator = sys.argv[2]
    y = sys.argv[3]

    if operator == "+":
        return functions.add(x, y)

    elif operator == "-":
        return functions.subtract(x, y)

    elif operator == "x":
        return functions.multiply(x, y)

    elif operator == "/":
        return functions.divide(x, y)

    else:
        return "invalid input"

if __name__ == "__main__":
    try:
        print(main())
    except ValueError as err:
        sys.stderr.write(err.args[0])
        sys.exit(1)
