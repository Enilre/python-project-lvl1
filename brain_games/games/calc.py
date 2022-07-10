"""Script for calculation for fisrt and second parameter."""
#!/usr/bin/env python


def calculate(num1, num2, expression):
    if expression == '+':
        return num1 + num2

    elif expression == '-':
        return num1 - num2

    elif expression == '*':
        return num1 * num2


if __name__ == '__main__':
    calculate()
