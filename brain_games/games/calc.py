"""Script for calculation for fisrt and second parameter."""
#!/usr/bin/env python


def calculate(num1, num2, expression):
    """Calculate resul of random numbers and expression.

    Args:
        num1: random number
        num2: random number
        expression: random expression

    Returns:
        return result of given numbers and expression.
    """
    if expression == '+':
        return num1 + num2

    elif expression == '-':
        return num1 - num2

    elif expression == '*':
        return num1 * num2


if __name__ == '__main__':
    calculate()
