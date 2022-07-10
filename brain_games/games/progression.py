"""Script for brain progression game."""

from random import *
from random import choice

def find_num():
    a = randint(0, 1000)
    c = randint(1, 10)
    b = a + (c * 10) 
    d = randint(0, 9)
    progression = list(range(a, b, c))
    for i in progression:
        correct_answer = choice(progression)
        hide_random_num = progression.index(correct_answer)
        progression[hide_random_num] = '..'
        print("Question:", ("{0}".format(' '.join(map(str, progression)))))
        return correct_answer
    
        

