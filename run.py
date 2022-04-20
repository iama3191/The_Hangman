from words import country_words
from stages import hangman
import random


def intro():
    """ 
    Greetings to the user explaining the rules and asking 
    for his name and a single character (Y or N) for 
    starting the game or exit the program
    """
    print('Welcome to the Hangman Game!!')
    print('Rules are simple: Guess the secret word in 8 tries or less\n')
    user_name = input('Enter your name: ').capitalize()
    start_game = input(f'{user_name} are you ready to play? (Y / N): ').upper()
    while start_game != 'N':
        if start_game == 'Y':
            print('Your word will be')
        else:
            start_game = input('Invalid input, try (Y or N): ')
            continue
        break   
intro()
