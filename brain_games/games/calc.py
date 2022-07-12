"""Script for calculation for fisrt and second parameter."""
from operator import add, mul, sub
from random import choice, randint

GAME_INTRO = 'What is the result of the expression?'
EXPRESSION = (('+', add), ('-', sub), ('*', mul))


def question_answer():
    """Calculate result of random numbers and expression.

    Args:
        No Args

    Returns:
        return result of given numbers and expression.
    """
    num1, num2 = randint(0, 100), randint(0, 100)
    random_expression = choice(EXPRESSION)
    question = '{0} {1} {2}'.format(num1, random_expression[0], num2)
    correct_answer = random_expression[1](num1, num2)
    return question, correct_answer
