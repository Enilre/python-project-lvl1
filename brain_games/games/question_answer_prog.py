"""Question and answer for brain progression game."""

from brain_games.games.greet import name  # welcome and ask user name
from brain_games.games.progression import find_num


def question_answer():
    """Play 3 rounds with user.

    Ask player question and get an answer.
    If answer is equal to result of correct answer
    play one more round. In total 3 rounds.
    If answer is not equal, break script.
    """
    print('What number is missing in the progression?')
    index = 1
    while index <= 3:
        missing_num = find_num()
        answer = input('Your answer is: ')
        if str(missing_num) == answer:
            print('Correct!')
            index += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet's try again, {2}!".format(answer, missing_num, name))
            return
    print('Congratulations, {0}!'.format(name))
