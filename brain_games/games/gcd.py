"""Script to find gcd for gcd game."""
from random import randint

GAME_INTRO = 'Find the greatest common divisor of given numbers.'


def question_answer():
    """Find gcd with Euclidean algorithm.

    While first number is not equal to second:
    Substract smaller number from greater
    until they become equal.

    Args:
        No arguments

    Returns:
        Return question, correct answer
    """
    num1, num2 = randint(0, 100), randint(0, 100)
    question = '{0} {1}'.format(num1, num2)

    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    correct_answer = num1
    return question, correct_answer
