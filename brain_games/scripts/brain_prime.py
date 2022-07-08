"""Brain-prime game"""
from random import *
from brain_games.games.greet import *  # welcoming and asking user name
from brain_games.games.prime import prime  # script for brain prime game


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    index = 1
    while index <= 3:
        random_num = randint(0, 100000)
        print(f'Question: {random_num}')
        guess = prime(random_num)
        answer = input('Your answer is: ')
        correct_answer = True if ((answer == 'yes' and guess == True) or (answer == 'no' and guess == False)) else False
        if correct_answer == True:
            print('Correct!')
            index += 1
        elif (correct_answer == False) and (guess == False):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            return
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

"""
        if (answer == 'yes' and guess == True) or (answer == 'no' and guess == False):
            print('Correct!')
            index += 1
        elif (answer != 'no' and guess == False):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            return
        elif (answer != 'yes' and guess == True):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
"""




if __name__ == '__main__':
    main()
