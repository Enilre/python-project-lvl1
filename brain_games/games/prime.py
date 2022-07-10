"""Find prime number."""


def find_prime(num):
    correct_answer = 'yes'
    number = 2
    while number * number <= num:
        if num % number == 0:
            correct_answer = 'no'
            break
        number += 1
    return correct_answer
