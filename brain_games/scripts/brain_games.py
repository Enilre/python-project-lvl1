"""Script for Brain Games."""
#!/usr/bin/env python
from brain_games.cli import welcome_user


def main():
    """Welcoming user and asking for name."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
    welcome_user()
