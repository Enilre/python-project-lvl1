"""Question and answer for brain progression game."""

from brain_games.games.greet import welcome_user, name, hello_user  # welcome and ask user name
from brain_games.games.progression import find_num  # script for find missing number


def question_answer():
    print('What number is missing in the progression?')
    
    """Run script."""
    index = 1
    while index <= 3:
        missing_num = find_num()
        answer = input('Your answer is: ')
        if str(missing_num) == answer:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{missing_num}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!') 
