"""Script for gcd game."""
import random
from random import randint


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
"""   
    index = 1
    while index <= 3:
        answer = input('Your answer is: ')
        if str(a) == answer:
            print('Correct!')
            index += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'\nLet's try again".format(answer, a))
            return
"""
