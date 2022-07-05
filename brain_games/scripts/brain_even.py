"""Script for the first Game - Brain even."""
#!/usr/bin/env python
from random import randint
import prompt


def main():
    """Welcoming user and asking for name."""
    print('Welcome to the Brain Games!')
    
    """Ask player a name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    """Run script for Brain even game."""
    index = 1
    while index <= 3:
        random_number = randint(0, 100)
        print('Question: {0}'.format(str(random_number)))
        answer = input('Your answer: ')
        correct_answer = True if ((random_number % 2 == 0) and (answer == 'yes')) or ((random_number % 2 != 0) and (answer == 'no')) else False
        if correct_answer is True:
            print('Correct!')
            index += 1
        elif (correct_answer is False) and (random_number % 2 == 0):
            print("'{0}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {1}!".format(answer, name))
            return
        else:
            print("'{0}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {1}!".format(answer, name))
            return
    print('Congratulations, {0}!'.format(name))


if __name__ == '__main__':
    main()
