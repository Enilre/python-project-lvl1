"""Question and answer script."""

from random import randint
from brain_games.games.greet import welcome_user, name, hello_user
from brain_games.games.prime import prime


def question_and_answer():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    index = 1
    while index <= 3:
        random_num = randint(0, 100000)  #changable range of random numbers
        print(f'Question: {random_num}')
        guess = prime(random_num)
        answer = input('Your answer is: ')
        correct_answer = bool((answer == 'yes' and guess) or (answer == 'no' and (not guess)))
        if correct_answer:
            print('Correct!')
            index += 1
        elif ((not correct_answer) and (not guess)):
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            return
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!') 
