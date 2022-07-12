"""Engine for brain-games modules."""
import prompt

GAME_ROUNDS = 3


def engine(module):
    """Script for brain-games.

    Welcome user, ask for his name, introduce to game and
    ask a question. User should give 3 correct answer or
    game will be over.

    Args:
        module: module of the game
    """
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')

    if name:
        print('Hello, {0}!'.format(name))
        print(module.GAME_INTRO)

        for _ in range(GAME_ROUNDS):
            question, correct_answer = module.question_answer()
            print('Question: {0}'.format(question))
            answer = prompt.string('Your answer is: ')
            if answer == str(correct_answer):
                print('Correct!')
                continue
            game_over(answer, correct_answer, name)
            return
        print('Congratulations, {0}!'.format(name))


def game_over(answer, correct_answer, name):
    """Run script if user gives wrong answer.

    Args:
        answer: user's answer
        correct_answer: result of given question
        name: user's name
    """
    reply_part1 = "'{0}' is wrong answer ;(. ".format(answer)
    reply_part2 = "Correct answer was '{0}'.".format(correct_answer)
    print(reply_part1 + reply_part2)
    print("Let's try again, {0}!".format(name))
