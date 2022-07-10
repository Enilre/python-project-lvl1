"""Script for the second Game - Brain calc."""
#!/usr/bin/env python
import random
from random import randint
from brain_games.games.greet import *  # script for welcome user and ask player a name
from brain_games.games.calc import calc  # script for brain calc game


"""Run script."""
def main():
    calc()

    
    if (correct_answer_sum is True) or (correct_answer_sub is True) or (correct_answer_multi is True):
        print('Correct!')
        index += 1
    elif random_expression == summing and correct_summing != answer:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, correct_summing, name))
        break
    elif random_expression == substraction and correct_sub != answer:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, correct_sub, name)) 
        break
    
    elif random_expression == multiply and correct_multiply != answer:
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, correct_multiply, name))break
    else:
        print('Congratulations, {0}!'.format(name))



if __name__ == '__main__':
    main()
