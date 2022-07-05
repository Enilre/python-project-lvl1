"""Logic for Brain Calc game"""
#!/usr/bin/env python
import random
from random import randint
from brain_games.games.greet import name  # import user name


def calc():
    print('What is the result of the expression?')
    summing = '+'
    substraction = '-'
    multiply = '*'
    expression = [summing, substraction, multiply]
    a = randint(1, 10)
    b = randint(1, 10)

    correct_summing = str(a + b)
    correct_sub = str(a - b)
    correct_multiply = str(a * b)

    index = 1
    while index <= 3:
        random_expression = random.choice(expression)
        print('Question: {0} {1} {2}'.format(a, random_expression, b))
        answer = input('Your answer: ')
        correct_answer_sum = True if (correct_summing == answer and random_expression == summing) else False
        correct_answer_sub = True if (correct_sub == answer and random_expression == substraction) else False
        correct_answer_multi = True if (correct_multiply == answer and random_expression == multiply) else False

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
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, correct_multiply, name))
            break
    else:
        print('Congratulations, {0}!'.format(name))

