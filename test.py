import random, re
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


def guess_is_alpha(user_input):
    """Check the user's input (letter or word)

    Arg: user_input (str) : The input from the user to guess
    the secret word

    Returns: boolean
    """
    if user_input.isalpha():
        return True
    else:
        return False


def check_in_used_letters(user_input, list_used_letters):
    """ Check if the input (it needs to be a character) is on the
    used_letters list

    Arg:
    - input (str) : the input as a single character to guess the
    secret word
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
    https://www.delftstack.com/howto/python/python-find-all-indexes-of-a-character-in-string/#:~:text=We%20can%20use%20the%20finditer,indexes%20where%20the%20pattern%20occurs.
    """
    l = user_input
    positions = [l.start() for l in re.finditer(l, word)]
    return positions


def list_to_string(list_letter):
    """ Transforms the items from a lit into a string, when the results
    are printed, they will show as characters with a space between them

    Arg: list_letter (list) : list that stored elements (letters)

    Returns: str 
    """
    convert = ', '
    list_letter.sort()
    return convert.join(list_letter)


def play_game():
    """Initialize the game and several functions are called to verify variables,
    in that way, the code is not repeated inside this function
    """
    player = intro()
    word = guess_word()
    tries = 7
    incorrect_letters = []
    correct_letters = []
    # I'm not sure if I will  use this variable or if I can remove it
    incorrect_words = []
    # Variable for knowing if the secret world is guessed
    is_correct = False
    word_length = ['_' for i in range(len(word))]
    print(player + '! your word has ' + str(len(word)) + ' letters\n')

    # loop that'll go until the try #7 and while user doesn't guess the word
    while tries > 0 and is_correct is False:
        used_letters = incorrect_letters + correct_letters
        print('\n< ========================================== >\n')
        print(f'Chances: {tries}\n')
        print(f'\t{word_length} {word}\n')
        print(f'Incorrect letters: {list_to_string(incorrect_letters)}')
        print(f'Correct letters: {list_to_string(correct_letters)}')
        print(f'Used letters: {list_to_string(used_letters)}\n')
        print(f'Incorrect words: {list_to_string(incorrect_words)}')
        player_guess = get_user_input('Enter a letter or the full word: ')
        validate_player_guess = guess_is_alpha(player_guess)
        char_used_letters = check_in_used_letters(player_guess, used_letters)

        if validate_player_guess and not char_used_letters:
            if len(player_guess) == 1:
                # match is a list with the indexes 
                match = letter_in_word(player_guess, word)
                if len(match) != 0:
                    print(f'Good job! {player_guess} is in the secret word')
                    correct_letters.append(player_guess)
                else:
                    tries -= 1
                    incorrect_letters.append(player_guess)
                    print(f'Sorry... {player_guess} is not in the secret word')
            elif len(player_guess) == len(word):
                if player_guess == word:
                    is_correct = True
                    print(f'{player}! You\'re a GENIUS! You got the word!')
                # if the word is the same, congrats, show a message 
                # for playing again
                else:
                    tries -= 1
                    incorrect_words.append(player_guess)
                    print(f'Sorry...{player_guess} is not the secret word')   
                
            else:
                print('Invalid input, a single character or full word')
                # user is not penalize for this, it will show a message 
                # offering help
        else:
            print('Invalid input, an alphabetic character or a new letter')

    if is_correct is False:
        print(f'{player} better luck the next time. The word was {word}')


play_game()
