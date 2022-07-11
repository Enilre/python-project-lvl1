"""Script to find gcd for gcd game."""


def find_gcd(num1, num2):
    """Find gcd with Euclidean algorithm.

    While first number is not equal to second:
    Substract smaller number from greater
    until they become equal.

    Parameters:
        num1: random number
        num2: random number

    Returns:
        Return num1 when it becomes equal to num2
    """
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1
