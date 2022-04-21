from words import country_words
from stages import hangman
import random

def get_user_input(message):
    """ Show  prompt to the user and get input from the user.

    Sanitize the input as follows
    - Remove leading and trailing spaces
    - Convert to uppercase the input for the later comparisons

    Arg: message (str) : The message asking for an input to the user

    Returns: str : The user's sanitized input.
    """

    user_input = input(message).strip().upper()
    return user_input

def intro():
    """Welcome the user to the Hangman Game, ask for the name 
    and show the rules of the game
    """
    print('''
    < ========================================== > \n
    Welcome to the Hangman Game!\n
    The rules are simple:\n
    1. Guess a random word (HINT: The theme is countries of the world)\n
    2. Enter one letter at a time or the full word \n
    3. Use only 7 tries until the hangman is completed\n
    4. Use only characters from the latin alphabet (vowels and consonants)\n
    < ========================================== > \n''')
    name = get_user_input('What is your name? ')
    print(f'\nI\'m so glad that you are here {name}! Let\'s play!!\n')
    return name


def guess_word():
    """
    Get a random word from the imported file words.py and return 
    the word in uppercase
    """
    return (random.choice(country_words)).upper()


def play_game():
    """
    Initialize the game, set variables and apply logic 
    for checking the inputs, decrease number of tries and print 
    statements for each round (incorrect letters, correct, letters,
    used letters)
    """
    player = intro()
    word = guess_word()
    tries = 7
    incorrect_letters = []
    # I'm not sure if I will  use this variable or if I can remove it
    incorrect_words = []
    correct_letters = []
    is_correct = False
    word_length = ['_' for i in range(len(word))]
    print(player + '! your word has ' + str(len(word)) + ' letters\n')
    # loop that'll go until the try #7 and while user doesn't guess the word
    while tries > 0  and is_correct is False:
        used_letters = incorrect_letters + correct_letters
        print('\n< ========================================== >\n')
        print(f'\t{word_length}\n')
        print(f'Chances: {tries}\n')
        print(f'Incorrect letters: {incorrect_letters}')
        print(f'Correct letters: {correct_letters}')
        print(f'Used letters: {used_letters}\n')
        player_guess = get_user_input('Enter a letter or the full word: ')
        # Condition to check if the character is in the latin alphabet 
        # and if is not in the used letters
        if player_guess.isalpha() and player_guess not in used_letters:
            # Condition to check if the user's input is a single character
            if len(player_guess) == 1:
                #Condition to check if the user's input is in the word
                if player_guess in word:
                    position = word.find(player_guess)
                    word_length[position] = player_guess
                    print(f'{player}! You did it! {player_guess} is in the word')
                    correct_letters.append(player_guess)
                else:
                    incorrect_letters.append(player_guess)
                    print(f'{player_guess} is not in the secret word')
                    tries -= 1
            elif len(player_guess) == len(word):
                if player_guess in word:
                    is_correct = True
                    print(f'{player}! {player_guess} is the secret word! Congrats!')
                else:
                    incorrect_words.append(player_guess)
                    print(f'Sorry... {player_guess} is not the secret word')
                    tries -= 1
            else:
                print(f'Sorry! {player_guess} is not the secret word')
                tries -= 1
        else:
            print(f'{player}, your input is not valid or you already used it')
        print(hangman[len(incorrect_letters)])
        if tries == 0:
            print('Better luck next time! You ran out of chances!')
            print(f'The word is {word}')


play_game()
