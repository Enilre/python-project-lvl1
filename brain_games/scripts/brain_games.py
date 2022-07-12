#!/usr/bin/env python3

"""Script for greeting user."""

from brain_games.cli import welcome_user


def main():
    """Welcoming user and asking for name."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
    welcome_user()
