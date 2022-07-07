"""Script for GCD game."""
import prompt
from random import randint
from brain_games.games.greet import *  # script for welcoming user
from brain_games.games.gcd import gcd



def main():
    print('Find the greatest common divisor of given numbers.')
    index = 1
    while index <= 3:
        num1 = randint(1, 1000)
        num2 = randint(1, 1000)
        print('Question: {0} {1}'.format(num1, num2))
        answer = input('Your answer is: ')
        gcd(num1, num2)
        correct_answer = gcd(num1, num2)
        if answer == str(correct_answer):
            print('Correct!')
            index += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, correct_answer, name))
            return
    print('Congratulations, {0}!'.format(name))



if __name__ == '__main__':
    main()
