"""Question and answer for brain calc game."""

from random import choice, randint

from brain_games.games.calc import calculate
from brain_games.games.greet import name


def question_answer():
    """Compare answer with result of calculate()."""
    index = 1
    while index <= 3:
        num1 = randint(0, 10)  # changable random numbers
        num2 = randint(0, 10)
        random_expression = choice(['+', '-', '*'])  # sum, substraction, multiply
        print('Question: {0} {1} {2}'.format(num1, random_expression, num2))
        answer = input('Your answer is: ')
        correct_answer = str(calculate(num1, num2, random_expression))
        if correct_answer == answer:
            print('Correct!')
            index += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, correct_answer, name))
            return
    print('Congratulations, {0}!'.format(name))
