"""Guess number is even or not."""
#!/usr/bin/env python


def even_or_not(number):
    """Guess number is even or not.

    Number is even when number divides by 2 with
    no rest.

    Args:
        number: random number

    Returns:
        Return yes or no if number is even or not.
    """
    return 'yes' if (number % 2 == 0) else 'no'
