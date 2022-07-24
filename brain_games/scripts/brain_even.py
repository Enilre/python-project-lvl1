#!/usr/bin/env python3

"""Brain even game."""

from brain_games.engine import run_engine
from brain_games.games import even


def main():
    """Run script for question and answer."""
    run_engine(even)


if __name__ == '__main__':
    main()
