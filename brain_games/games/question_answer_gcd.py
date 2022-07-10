"""Question and answer for brain gcd game."""

from random import randint

from brain_games.games.greet import name  # script for welcoming user
from brain_games.games.gcd import find_gcd  # script for find gcd


def question_answer():
    print('Find the greatest common divisor of given numbers.')

    index = 1
    while index <= 3:
        num1 = randint(1, 1000)  #changable random numbers
        num2 = randint(1, 1000)
        print(f'Question: {num1} {num2}')
        answer = input('Your answer is: ')

        """Run script."""
        correct_answer = find_gcd(num1, num2)
        if answer == str(correct_answer):
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
