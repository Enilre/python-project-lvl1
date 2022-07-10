"""Question and answer for brain even game."""
from brain_games.games.greet import welcome_user, name, hello_user  # welcome and ask user name
from brain_games.games.even import even_or_not  # find if number is even or not
from random import randint


def even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 1
    while index <= 3:
        random_num = randint(1, 100)
        print(f'Question: {random_num}')
        answer = input('Your answer is: ')

        """Return even or not number."""
        guess = even_or_not(random_num)
        correct_answer = 'yes' if (guess == True) else 'no'
        if correct_answer == answer:
            print('Correct!')
            index += 1
        elif correct_answer != answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

