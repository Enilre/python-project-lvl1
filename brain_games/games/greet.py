"""Script for greet user and ask for name."""
#!/usr/bin/env python
import prompt

print('Welcome to the Brain Games!')
name = prompt.string('May I have your name? ')
print('Hello, {0}!'.format(name))

