#!/usr/bin/env python3

"""Script for the second Game - Brain calc."""

from brain_games.engine import run_engine
from brain_games.games import calc


def main():
    """Run script for question and answer."""
    run_engine(calc)


if __name__ == '__main__':
    main()
