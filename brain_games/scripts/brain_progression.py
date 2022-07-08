"""Script for Brain progression."""
from brain_games.games.greet import *  # welcominh user
from brain_games.games.progression import prog

def main():
    index = 1
    print('What number is missing in the progression?')
    while index <= 3:
        a = prog()
        answer = input('Your answer is: ')
        if str(a) == answer:
            print('Correct!')
            index += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{a}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()

