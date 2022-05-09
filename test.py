"""
Importing the libraries to use in system
"""
import random
import re
import sys
from words import country_words
from stages import hangman


def get_user_input(message):
    """ Show  prompt to the user and get input from the user.

    Sanitize the input as follows:
    - Remove leading and trailing spaces
    - Convert to uppercase the input for the later comparisons

    Arg: message (str) : The message asking for an input to the user

    Returns: str : The user's sanitized input.
    """
    user_input = input(message).strip().upper()
    return user_input


def rules_help():
    """ Show rules to the user

    Returns : rules (str): The rules for understanding the game
    """
    rules = ''' \n <------------------------------------------------------------>
    \n \033[3;33m Rules: \033[0;0m \n
 The Hangman is a very simple game, where you need to think logically,
 to become the winner. The theme of the game is: 'Countries of the World'.\n
    1. A random word is generated from a list of 157 countries.\n
    2. You can enter one letter at the time or you can try to complete the
 whole word.\n
    3. You have only 8 tries to discover the hidden word.\n
    4. You can only use characters from the latin alphabet (vowels and
 consonants).
    \n\033[3;33m YOU WON'T BE PENALIZED FOR THE FOLLOWING CASES: \033[0;0m \n
    1. Enter a number or a symbol.\n
    2. Enter a word with a different length than the secret word. \n
    3. Enter a letter that has already been used.
    \n <------------------------------------------------------------>\n'''
    return rules


def validation_user_name(mssg):
    """Validate the user's name so the user can enter an alphanumeric name.
    And the input needs to be longer than one character.

    Arg: mssg (str): Message asking a name to the user

    Returns: user_name(str): user's input is capitalized
    """
    user_name = input(mssg).strip()
    while not user_name.isalnum() or len(user_name) == 1:
        print('\n Invalid input... Please use alphanumeric characters, and'
              ' the name needs to have more than "1" character.\n')
        user_name = input(mssg).strip()
    return user_name.capitalize()


def intro():
    """Welcome the user to the Hangman Game, ask for the name
    and show the rules of the game
    """
    print('''\n __/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\'''
          '''__/\\__/\\__\n
 Welcome to The Hangman Game!! If you want to win, you only need to guess the
 hidden word.\n''')
    name = validation_user_name(' What is your name? (You can use numbers and'
                                ' letters)\033[1;33m ---> \033[0;0m')
    while True:
        print('''\n \033[3;33m***** Main menu *****\033[0;0m \n
        \033[1;33m(1)\033[0;0m HELP\n
        \033[1;32m(2)\033[0;0m PLAY\n
        \033[1;31m(3)\033[0;0m EXIT
        ''')
        answer = get_user_input(f' {name}! Please select "1" for checking the'
                                ' rules, "2" for starting the game or "3" for'
                                ' exiting the game \033[1;33m ---> \033[0;0m')
        try:
            answer = int(answer)
        except ValueError:
            print(f'\n\033[1;31m -->\033[0;0m Invalid input: {answer}')
        else:
            if answer == 1:
                game_rules = rules_help()
                print(game_rules)
            elif answer == 2:
                print(f'\n Good luck, {name}! New game is starting...\n')
                return name
            elif answer == 3:
                exit_game(name)
                print('\n You\'re returning to the main menu...')
            else:
                print('\n\033[1;31m -->\033[0;0m Invalid input. Please enter'
                      ' "1", "2" or "3"')
                continue


def guess_word():
    """Get a random word from the imported file words.py

    Returns: random_word (str): A string in uppercase
    """
    random_word = (random.choice(country_words)).upper()
    return random_word


def guess_is_alpha(user_input):
    """Check the user's input (letter or word) and verify if the input
    is an alphabetic string without numbers and symbols:',./$#'

    Arg: user_input (str) : The input from the user to guess
    the secret word

    Returns: boolean: Returns True or False
    """
    if user_input.isalpha():
        return True
    else:
        return False


def check_in_used_letters(player_guess, used_letters):
    """ Check if the input (a character) is on the
    used_letters list

    Arg:
    - player_guess (str) : the input as a alphabetic character
    - used_letters (list) : list with all the letters that
    the user is already used

    Returns: boolean
    """
    if player_guess in used_letters:
        return True
    else:
        return False


def letter_in_word(player_guess, word):
    """ Check if the letter entered from the user is in the word,
    and  in what positions are they

    Arg:
    - player_guess (str) : user's input for guessing the word
    - word (str) : the secret word that the user needs to guess
    Returns: positions (list) : with the indexes where the ocurrences existed

    This code is from the next link:
    https://www.delftstack.com/howto/python/python-find-all-indexes-of-a-
    character-in-string/#:~:text=We%20can%20use%20the%20finditer,indexes%20
    where%20the%20pattern%20occurs.
    """
    letter = player_guess
    positions = [letter.start() for letter in re.finditer(letter, word)]
    return positions


def list_to_string(list_letter):
    """ Transforms the items from a lit into a string, when the results
    are printed, they will be shown as characters with a comma and a space
    between them alphabetically

    Arg: list_letter (list) : list that stored elements (letters or words with
    the same length as the hidden word)

    Returns: str: all the letters ordered alphabetically

    This code is from the next link:
    https://stackoverflow.com/questions/49463141/how-to-print-a-list-like-a-string
    """
    convert = '  '
    list_letter.sort()
    return convert.join(list_letter)


def display_messages(
    player,
    word,
    tries,
    dupl_word_length,
    incorrect_letters,
    correct_letters,
    used_letters,
    incorrect_words
):
    """ Print all the neccessary messages to the user for each round

    Arg:
    - player (str): Chosen name by the user.
    - word (str): Random country from the list country_words.
    - tries (num): The maximun number of tries before the hangman is completed.
    - dupl_word_length (str): Chosen word that will be displayed with a space
    between each letter.
    - incorrect_letters (lst): list with all the entered letters that aren't
    in the hidden word.
    - correct_letters (lst): list with all the entered letters that are in
    the words.
    - used_letters (lst): list with all the entered letters by the user
    (correct and incorrect letters)
    - incorrect_words (lst): list with all the words with the same length
    as the hidden word that aren't correct
    """
    print(' ______________\n')
    print('\033[1;31m Choose "1" for checking the rules, "2" for '
          'restarting, and "3" for exiting the game...\033[0;0m \n')
    print(f'\t\t\t\t\033[1;33m** You have {tries} tries **\033[0;0m\n')
    print(f'\n {player}! your word has {str(len(word))} letters:'
          f'  {dupl_word_length}\n')
    print(f'\n\033[1;31m Incorrect letters: '
          f'{list_to_string(incorrect_letters)}\033[0;0m\n')
    print(f'\033[1;32m Correct letters: '
          f'{list_to_string(correct_letters)}\033[0;0m\n')
    print(f'\033[1;37m Used letters: '
          f'{list_to_string(used_letters)}\033[0;0m\n')
    print(f'\033[1;31m Incorrect words: '
          f'{list_to_string(incorrect_words)}\033[0;0m')
    print(f'{hangman[len(incorrect_letters + incorrect_words)]}\n')


def restart_game(player, game_is_done):
    """show message to the user for a new game after the game is over.
    (No matter if he wins or loses).

    Arg: player(str): name of the user for displaying personal messages.
    """
    while game_is_done:
        play_again = get_user_input(' Would you like to play a new'
                                    ' game, "Y" or "N"?\033[1;33m ---> '
                                    '\033[0;0m')
        if play_again == 'Y':
            print('\n A new game is starting....\n')
            start_game(player, game_is_done)
            return game_is_done
        elif play_again == 'N':
            game_is_done = False
            return game_is_done
        else:
            print('\n\033[1;31m -->\033[0;0m Invalid input... "Y" or "N": ')


def exit_game(player):
    """Validate the user's answer when he wants to exit, in case he makes
    a mistake entering the number '3' when he didn't want to.

    Arg: player (str): user's name for a more personal approach"""
    while True:
        question_exiting_game = get_user_input(f'\n {player}, are you sure'
                                               f' you want to exit the '
                                               f'game? "Y" or "N": ')
        if question_exiting_game == 'Y':
            print('\n You\'re exiting the game...\n')
            print(f' {player}, see you next time!\n')
            print(' __/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\__/\\'
                  '__/\\__/\\__/\\__/\\__\n')
            sys.exit(0)
        elif question_exiting_game == 'N':
            return
        else:
            print('\n\033[1;31m -->\033[0;0m Invalid input... "Y" or "N": ')


def start_game(new_player, game_is_done):
    """Initialize the game and several functions are called to verify variables.

    Arg:
    - new_player (str): Name chosen by the user
    - game_is_done (boolean): is the game over
    """
    player = new_player
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
        display_messages(
            player,
            word,
            tries,
            dupl_word_length,
            incorrect_letters,
            correct_letters,
            used_letters,
            incorrect_words)
        player_guess = get_user_input(f' Enter a letter or a word with'
                                      f' {len(word)} letters\033[1;33m '
                                      f'---> \033[0;0m')
        validate_player_guess = guess_is_alpha(player_guess)
        char_used_letters = check_in_used_letters(player_guess, used_letters)
        if validate_player_guess and not char_used_letters:
            # condition to check user's input based on the length (a char, word
            # with the same length as the hidden word or a word with
            # different length)
            if len(player_guess) == 1:
                match = letter_in_word(player_guess, word)
                if len(match) != 0:
                    for element in match:
                        word_length[element] = player_guess
                    print(f'\n GREAT! {player_guess} is in the secret word\n')
                    correct_letters.append(player_guess)
                else:
                    tries -= 1
                    incorrect_letters.append(player_guess)
                    print(f'\n Sorry... {player_guess} is not in the'
                          f' secret word \n')
            elif len(player_guess) == len(word):
                if player_guess == word:
                    is_correct = True
                    game_is_done = True
                elif player_guess != word:
                    tries -= 1
                    incorrect_words.append(player_guess)
                    print(f'\n Sorry...{player_guess} is not the secret'
                          f' word \n')
                else:
                    print('\n\033[1;31m -->\033[0;0m Invalid input, enter'
                          ' a single letter or the complete word\n')
            else:
                print('\n The word has a different length of the hidden word')
        else:
            if player_guess == '1':
                print(f'\n {player}... Check the rules... \n')
                rules = rules_help()
                print(rules)
                print('\n Game is continuing...\n')
            elif player_guess == '2':
                game_is_done = True
                resume_game = restart_game(player, game_is_done)
                if resume_game is False:
                    print('\n Returning to the game...')
                else:
                    break
            elif player_guess == '3':
                exit_game(player)
            else:
                print('\n\033[1;31m -->\033[0;0m Invalid input, please '
                      'enter a new letter.\n')
        # Code from https://mardiyyah.medium.com/a-simple-hangman-
        # learnpythonthroughprojects-series-10-fedda58741b
        status = ''
        if is_correct is False:
            for letter in word:
                if letter in correct_letters:
                    status += letter
                else:
                    status += '_'
        if status == word:
            is_correct = True
        # End of the used code
    if tries == 0:
        print(hangman[len(incorrect_letters)])
        print(f'\n {player}! The word was {word}\n')
    if is_correct is True:
        print(f'\n {player}! You\'re a GENIUS! {word} is the '
              f'hidden word\n')


def main():
    """Initialize the game and restart after each round if t
    he user wants to do it"""
    game_is_done = False
    new_player = intro()
    while game_is_done is False:
        start_game(new_player, game_is_done)
        while True:
            end_game = get_user_input(f'\n {new_player}, would you like to '
                                      f'play again? "Y" or "N" ')
            if end_game == 'N':
                game_is_done = True
                break
            elif end_game == 'Y':
                break
            else:
                print('\n Invalid input... "Y" or "N" ')
            game_is_done = False
    print('\n Thank for playing, see you next time...')


main()
