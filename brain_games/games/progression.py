"""Script for brain progression game."""
from random import randint, choice


def find_num():
    length_progression = 10
    random_start_range = randint(0, 1000)
    random_step_range = randint(1, 10)
    random_finish_range = random_start_range + (random_step_range * length_progression)

    progression = list(range(random_start_range, random_finish_range, random_step_range))
    correct_answer = choice(progression)
    hide_random_num = progression.index(correct_answer)
    progression[hide_random_num] = '..'
    print('Question:', ('{0}'.format(' '.join(map(str, progression)))))
    return correct_answer
