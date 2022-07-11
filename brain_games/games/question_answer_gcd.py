"""Question and answer for brain gcd game."""
from random import randint

from brain_games.games.gcd import find_gcd
from brain_games.games.greet import name


def question_answer():
    """Find gcd and compare it with user answer.

    Find gcd of two random numbers.
    Return result after comparison between gcd and user answer.

    """
    print('Find the greatest common divisor of given numbers.')
    index = 1
    while index <= 3:
        num1 = randint(1, 1000)  # changable random numbers
        num2 = randint(1, 1000)
        print('Question: {0} {1}'.format(num1, num2))
        answer = input('Your answer is: ')

        correct_answer = find_gcd(num1, num2)
        if answer == str(correct_answer):
            print('Correct!')
            index += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, correct_answer, name))
            return
    print('Congratulations, {0}!'.format(name))
