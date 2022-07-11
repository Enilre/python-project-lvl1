"""Script for brain progression game."""
from random import choice, randint


def find_num():
    """Random progression with random range.

    Returns:
        Return randomly chosen number in progression.
    """
    length = 10
    random_start = randint(0, 1000)
    random_step = randint(1, 10)
    random_finish = random_start + (random_step * length)

    progression = list(range(random_start, random_finish, random_step))
    correct_answer = choice(progression)
    hide_random_num = progression.index(correct_answer)
    progression[hide_random_num] = '..'
    print('Question:', ('{0}'.format(' '.join(map(str, progression)))))
    return correct_answer
