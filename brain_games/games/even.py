"""Script for brain even game."""
#!/usr/bin/env python
import prompt 
from random import randint
from brain_games.games.greet import welcome_user, name, hello_user  # welcome and ask user name

def even_or_not(a):
    correct_answer = True if (a % 2 == 0) else False 
    return correct_answer
