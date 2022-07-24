#!/usr/bin/env python3

"""Script for GCD game."""

from brain_games.engine import run_engine
from brain_games.games import gcd


def main():
    """Run script."""
    run_engine(gcd)


if __name__ == '__main__':
    main()
