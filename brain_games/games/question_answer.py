"""Question and answer script."""

from random import randint

from brain_games.games.greet import name
from brain_games.games.prime import guess_prime


def question_answer():
    """Compare answer and result of find_prime()."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    index = 1
    while index <= 3:
        random_num = randint(0, 1000)  # changable range of random numbers
        print('Question: {0}'.format(random_num))
        correct_answer = guess_prime(random_num)
        answer = input('Your answer is: ')
        if correct_answer == answer:
            print('Correct!')
            index += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, correct_answer, name))
            return
    print('Congratulations, {0}!'.format(name))
