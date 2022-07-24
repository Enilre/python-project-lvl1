"""Script for brain progression game."""
from random import choice, randint

GAME_INTRO = 'What number is missing in the progression?'


def ask_question_get_answer():
    """Random progression with random range.

    Returns:
        Return randomly chosen number in progression.
    """
    start, step = randint(0, 1000), randint(1, 10)
    finish = start + (step * 10)
    progression = list(range(start, finish, step))
    correct_answer = choice(progression)

    progression[progression.index(correct_answer)] = '..'
    question = '{0}'.format(' '.join(map(str, progression)))
    return question, str(correct_answer)
