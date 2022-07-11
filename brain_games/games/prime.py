"""Script to find prime number for brain prime game."""


def guess_prime(num):
    """Guess prime number or not.

    Number is prime if number is divided without rest
    only by 1 and by number itself.

    Args:
        num: random number

    Returns:
        return yes or no if number is prime or not.
    """
    correct_answer = 'yes'
    number = 2
    while number * number <= num:
        if num % number == 0:
            correct_answer = 'no'
            break
        number += 1
    return correct_answer
