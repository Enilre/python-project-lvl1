"""Script for greeting in Brain games."""
import prompt


def welcome_user():
    """Ask a player name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # print('Hello, ' + name + '!')
