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
    print(f'\nI\'m so glad that you are here {name}! Let\'s play and have fun!!\n')
    return name


def guess_word():
    """
    Get a random word from the imported file words.py and return the word in uppercase
    """
    return (random.choice(country_words)).upper()


def play_game():
    """
    Initialize the game, set variables (tries, used letters, )
    """
    player = intro()
    word = guess_word()
    tries = 8
    round = 0
    incorrect_letters = []
    correct_letters = []
    is_correct = False
    word_length = '_ ' * len(word)
    print('< ========================================== > \n')
    print(f'\t{word_length}\n')
    print(player + '! your word has ' + str(len(word)) + ' letters')


play_game()