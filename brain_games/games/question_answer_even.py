"""Question and answer for brain even game."""

from random import randint

from brain_games.games.even import even_or_not
from brain_games.games.greet import name


def question_answer():
    """Compare answer with result of even_or-not()."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 1
    while index <= 3:
        random_num = randint(1, 100)
        print('Question: {0}'.format(random_num))
        answer = input('Your answer is: ')
        correct_answer = even_or_not(random_num)
        if correct_answer == answer:
            print('Correct!')
            index += 1
        elif correct_answer != answer:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, correct_answer, name))
            return
    print('Congratulations, {0}!'.format(name))
