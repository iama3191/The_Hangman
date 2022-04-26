import random
import re
from words import country_words
from stages import hangman


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


def rules_help():
    """ Show rules to the user
    Arg: name (str) : Name of the user to display in print statements
    """
    rules = ''' \n<------------------------------------------------------------>
    \n \033[3;33m Rules: \033[0;0m \n
The Hangman is a very simple game, where you need to think logically,
to become the winner. The theme of the game is: 'Countries of the World'.\n
    1. A random word is generated from a list of 157 countries.\n
    2. You can enter one letter at the time or you can try to complete the
whole word.\n
    3. You have only 8 tries to discover the secret country.\n
    4. You can only use characters from the latin alphabet (vowels and
consonants).
    \n\033[3;33m YOU WON'T BE PENALIZED FOR THE FOLLOWING CASES: \033[0;0m \n
    1. Enter a numeric character or a symbol.\n
    2. Enter a word with a different length than the secret word. \n
    3. Enter a letter that has already been used.
    \n<------------------------------------------------------------>\n'''
    return rules


def intro():
    """Welcome the user to the Hangman Game, ask for the name
    and show the rules of the game
    """
    print('''\n__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__\n
Welcome to The Hangman Game!! If you want to win, you only need to guess the
hidden word.\n''')
    name = (get_user_input('What is your name? \033[1;33m ---> \033[0;0m \n')).capitalize()
    while True:
        print('''\n\033[1;33m Main menu: \033[0;0m \n
        \033[1;33m(1)\033[0;0m HELP\n
        \033[1;32m(2)\033[0;0m PLAY\n
        \033[1;31m(3)\033[0;0m EXIT\n
        ''')
        answer = get_user_input(f'{name}! Please select "1" for checking the rules, "2" for starting the game or "3" for exiting the game \033[1;33m ---> \033[0;0m \n')
        try:
            answer = int(answer)
            if answer == 1:
                game_rules = rules_help()
                print(game_rules)
            elif answer == 2:
                play_game(name)
                break
            elif answer == 3:
                print(f'\n{name} see you next time!')
                break
            else:
                print('\n\033[1;31m -->\033[0;0m Invalid input. Please enter "1", "2" or "3"')
                continue
        except:
            print('\n\033[1;31m -->\033[0;0m Invalid input. Please enter "1", "2" or "3"')
        

def guess_word():
    """Get a random word from the imported file words.py

    Returns: random_word (str): A string in uppercase
    """
    random_word = (random.choice(country_words)).upper()
    return random_word


def guess_is_alpha(user_input):
    """Check the user's input (letter or word) and verify if the input
    is an alphabetic string without numbers and symbols:',./...'

    Arg: user_input (str) : The input from the user to guess
    the secret word

    Returns: boolean
    """
    if user_input.isalpha():
        return True
    else:
        return False


def check_in_used_letters(user_input, list_used_letters):
    """ Check if the input (a character) is on the
    used_letters list

    Arg:
    - input (str) : the input as a alphabetic character
    -list_used_letters (list) : list with all the letters that
    the user is already used

    Returns: boolean
    """
    if user_input in list_used_letters:
        return True
    else:
        return False


def letter_in_word(user_input, word):
    """ Check if the letter entered from the user is in the word,
    and  in what positions are they
    Arg:
    - user_input (str) : user's input for guessing the word
    -word (str) : the secret word that the user needs to guess

    Returns: positions (list) : with the indexes where the ocurrences existed

    This code is from the next link:
    https://www.delftstack.com/howto/python/python-find-all-indexes-of-a-character-in-string/#:~:text=We%20can%20use%20the%20finditer,indexes%20where%20the%20pattern%20occurs.
    """
    letter = user_input
    positions = [letter.start() for letter in re.finditer(letter, word)]
    return positions


def list_to_string(list_letter):
    """ Transforms the items from a lit into a string, when the results
    are printed, they will show as characters with a comma and a space between
    them alphabetically

    Arg: list_letter (list) : list that stored elements (letters or words with the same length as the hidden word)

    Returns: str

    This code is from the next link:
    https://stackoverflow.com/questions/49463141/how-to-print-a-list-like-a-string
    """
    convert = '  '
    list_letter.sort()
    return convert.join(list_letter)


def display_messages(player, word, tries, dupl_word_length, incorrect_letters, correct_letters, used_letters, incorrect_words):
    """ Print all the neccessary messages to the user for each round
    """
    print('\n__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__\n')
    print(f'\033[1;33m Chances: {tries}\033[0;0m\n')
    print(f'{player}! your word has {str(len(word))} letters\n')
    print(f'\nThe hidden word is \t{dupl_word_length}\n')
    print(f'\n\033[1;31m Incorrect letters: {list_to_string(incorrect_letters)}\033[0;0m\n')
    print(f'\033[1;32m Correct letters: {list_to_string(correct_letters)}\033[0;0m\n')
    print(f'\033[1;37m Used letters: {list_to_string(used_letters)}\033[0;0m\n')
    print(f'\033[1;31m Incorrect words: {list_to_string(incorrect_words)}\033[0;0m')
    print(f'{hangman[len(incorrect_letters + incorrect_words)]}\n')


def play_new_game(player):
    """show message to the user for a new game after the game is over.
    (No matter if he wins or loses).
    Arg: player(str): name of the user for displaying personal messages.
    """
    play_again = get_user_input(f'\n{player}, would you like to play a new game, "Y" or "N"?\033[1;33m ---> \033[0;0m')
    if play_again == 'Y':
        play_game(player)
    elif play_again == 'N':
        print(f'\n{player}! Thank you for playing! See you later!\n')
        print('\n__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__\n')
        return
    else:
        print('\n\033[1;31m -->\033[0;0m Invalid input, please enter, "Y" or "N"')


def play_game(name):
    """Initialize the game and several functions are called to verify variables,
    in that way, the code is not repeated inside this function
    """
    player = name
    word = guess_word()
    tries = 8
    incorrect_letters = []
    correct_letters = []
    incorrect_words = []
    is_correct = False
    word_length = ['_' for i in range(len(word))]

    # loop that'll go until the try #8 and while user doesn't guess the word
    while tries > 0 and is_correct is False:
        used_letters = incorrect_letters + correct_letters
        dupl_word_length = ' '.join(word_length)
        display_messages(player, word, tries, dupl_word_length, incorrect_letters, correct_letters, used_letters, incorrect_words)
        player_guess = get_user_input('Enter a letter or the full word \033[1;33m ---> \033[0;0m')
        validate_player_guess = guess_is_alpha(player_guess)
        char_used_letters = check_in_used_letters(player_guess, used_letters)
        if validate_player_guess and not char_used_letters:
            # condition to check user's input based on the length (a char, word
            # with the same length as the hidden word and a word with
            # different length)
            if len(player_guess) == 1:
                match = letter_in_word(player_guess, word)
                if len(match) != 0:
                    for element in match:
                        word_length[element] = player_guess
                    print(f'\nGood job! {player_guess} is in the secret word\n')
                    correct_letters.append(player_guess)
                else:
                    tries -= 1
                    incorrect_letters.append(player_guess)
                    print(f'\nSorry... {player_guess} is not in the secret word \n')
            elif len(player_guess) == len(word):
                if player_guess == word:
                    is_correct = True
                    print(f'\n{player}! You\'re a GENIUS! You got the word!\n')
                    play_new_game(player)
                elif player_guess != word:
                    tries -= 1
                    incorrect_words.append(player_guess)
                    print(f'\nSorry...{player_guess} is not the secret word \n')
                else:
                    print('\n\033[1;31m -->\033[0;0m Invalid input, enter a single letter or the complete word\n')
        else:
            print('\n\033[1;31m -->\033[0;0m Invalid input, please enter a new letter.\n')
        status = ''
        if is_correct is False:
            for letter in word:
                if letter in correct_letters:
                    status += letter
                else:
                    status += '_'
        if status == word:
            print(f'\nCongrats! You did it! {word} is the hidden country')
            play_new_game(player)
            is_correct = True
    if is_correct is False:
        print(hangman[len(incorrect_letters)])
        print(f'\n{player} better luck the next time. The word was {word}\n')
        play_new_game(player)


intro()
