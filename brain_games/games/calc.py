"""Script for calculation for fisrt and second parameter."""
from operator import add, mul, sub
from random import choice, randint

GAME_INTRO = 'What is the result of the expression?'
EXPRESSION = (('+', add), ('-', sub), ('*', mul))


def ask_question_get_answer():
    """Calculate result of random numbers and expression.

    Args:
        No Args

    Returns:
        return result of given numbers and expression.
    """
    num1, num2 = randint(0, 100), randint(0, 100)
    symbol_operator, expression = choice(EXPRESSION)
    question = '{0} {1} {2}'.format(num1, symbol_operator, num2)
    correct_answer = expression(num1, num2)
    return question, str(correct_answer)
