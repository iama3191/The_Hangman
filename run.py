from words import country_words
from stages import hangman
import random


def intro():
    """
    Welcome the user to the Hangman Game, ask for the name, explain the 
    rules and calls for the game function
    """
    print('''
    < ========================================== > \n
    Welcome to the Hangman Game!\n
    The rules are simple:\n
    1. You need to guess a random word (HINT: The theme is countries of the world)\n
    2. You have 8 tries until the hangman is completed\n
    3. You can use only characters from the latin alphabet (vowels and consonants)\n
    < ========================================== > \n''')
    name = input('What is your name? ').capitalize()
    print(f'\nI\'m so glad that you are here {name}! Let\'s play and have fun!!')
    #start_game()


def guess_word():
    """
    Get a random word from the imported file words.py and return the word in uppercase
    """
    word = random.choice(country_words)
    print(word.upper())


intro()
guess_word()
