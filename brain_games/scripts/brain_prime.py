#!/usr/bin/env python3

"""Brain-prime game."""

from brain_games.engine import run_engine
from brain_games.games import prime


def main():
    """Script for question and answer from user."""
    run_engine(prime)


if __name__ == '__main__':
    main()
