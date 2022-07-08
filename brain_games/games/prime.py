"""Script for Brain prime game."""
from random import *

def prime(num):

    correct_answer = True
    d = 2
    while d * d <= num:
        if num % d == 0:
            correct_answer = False
            break
        d += 1
    return correct_answer

