"""Script of progression."""

from random import *
from random import choice
def prog():
    a = randint(0, 1000)
    c = randint(1, 10)
    b = a + (c * 10) 
    d = randint(0, 9)
    progression = list(range(a, b, c))
    for i in progression:
        correct_answer = choice(progression)
        d = progression.index(correct_answer)
        progression[d] = '..'
        print("Question:", ("{0}".format(' '.join(map(str, progression)))))
        return correct_answer
    
        

