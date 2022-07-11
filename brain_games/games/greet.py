"""Script for greet user and ask for name."""
#!/usr/bin/env python
import prompt

welcome_user = print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
hello_user = print('Hello, {0}!'.format(name))
