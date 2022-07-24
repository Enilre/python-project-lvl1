"""Guess number is even or not."""

from random import randint

GAME_INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def ask_question_get_answer():
    """Guess number is even or not.

    Number is even when number divides by 2 with
    no rest.

    Args:
        No arguments

    Returns:
        Return correct_answer, question
    """
    number = randint(0, 100)
    question = '{0}'.format(number)
    correct_answer = 'yes' if (number % 2 == 0) else 'no'
    return question, str(correct_answer)
