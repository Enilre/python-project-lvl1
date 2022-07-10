"""Question and answer for brain calc game."""

from random import randint, choice

from brain_games.games.greet import name  # script for welcome and ask user name
from brain_games.games.calc import calculate  # script to calculate by given expression


def question_answer():
    index = 1
    while index <= 3:
        num1 = randint(0, 10)  # changeable random numbers
        num2 = randint(0, 10)
        expression = ['+', '-', '*']  # sum, substraction, multiply
        random_expression = choice(expression)
        print(f'Question: {num1} {random_expression} {num2}')
        answer = input('Your answer is: ')
        """Run script."""
        correct_answer = str(calculate(num1, num2, random_expression))
        if correct_answer == answer:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
