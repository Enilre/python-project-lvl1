"""Script to find prime number for brain prime game."""
from random import randint

GAME_INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_answer():
    """Guess prime number or not.

    Number is prime if number is divided without rest
    only by 1 and by number itself.

    Args:
        No arguments

    Returns:
        return yes or no if number is prime or not.
    """
    random_number = randint(0, 100)
    question = '{0}'.format(random_number)
    correct_answer = 'yes'
    number = 2
    while number * number <= random_number:
        if random_number % number == 0:
            correct_answer = 'no'
            break
        number += 1
    return question, correct_answer
