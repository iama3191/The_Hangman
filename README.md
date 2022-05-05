# The Hangman

![Am I respondive photo](relative path)

[Link to Website](https://countries-hangman.herokuapp.com/)

[GitHub Repo](https://github.com/iama3191/hangman)

## About
The Hangman is a guessing game for two or more players. One player chooses a word, a phrase or a sentence, and the rest of the players try to guess by indicating letters or if they are feeling confident, indicating the full word, phrase or sentence.  
The word to guess is represented by a row of dashes representing each letter of the word. If the suggested letter is in the word, it is written down in all its correct positions. If it isn't in the word, the player, who chose the word, draws a stage of the hangman. This process is repeated until the hangman's diagram is completed. The number of tries  can change depending on how detailed is the diagram.
This game is adapted for playing against the computer. All the words belong to the theme: 'Countries of the world', the player has 8 tries until the hangman is completed


## Index - Table of Contents
* [The Hangman](#the-hangman)
* [About](#about)
* [Index - Table of Contents](#index---table-of-contents)
* [User Experience Research and Design](#user-experience-research-and-design)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
* [Features](#features)
    * [Current Features](#current-features)
    * [Future Features](#future-features)
* [Testing](#testing)
    * [User Stories](#user-stories)
    * [Functionality](#functionality)
* [Deployment](#deployment)
    * [Fork and Deploy with GitHub](#fork-and-deploy-with-github)
    * [Deploy with Heroku](#deploy-with-heroku)
* [Credit](#credit)
    * [People](#people)
    * [Python Library Dependecies and Packages](#python-library-dependecies-and-packages)
    * [Software & Web Applications](#software--web-applications)


## User Experience Research and Design

### Strategy

* Reasons a user may want to visit the website

    - To play a guessing game as a single player with a limited number of tries.

    - To test his knowledge about countries of the world.

* Reasons for the website

    - Giving to the user the chance to guess the hidden country within 8 tries.

    - Giving to the user the possibility to test how many countries he knows.

### Scope

* What a user may expect

    - Clear instructions to play the game

    - Clear information on how many attempts he has, what letters he has used, warning messages when something went wrong, updated hangman stage.

* What a user may want

    - The possibility to restart the game at any time of the game.

    - The possibility to ask for help at any time of the game.

    - The possibility to exit the game at any time of the game.

    - That the words in the game belong to a specific category.

* As a developer what I expect

    - The user finds an entertaining game and easy to play.

    - Well-commented code for easy maintenance.

### Structure

### Skeleton

### Surface

## Features

### Current Features

### Future Features

## Testing

### User Stories

### Functionality

|                      Test Label                     |                                                                        Test Action                                                                      |                                                                                                                                                      Expected Outcome                                                                                                                                                     |   Test Outcome  |
|:-------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------:|
|                 Validation of user’s name                |   User enters an alphanumeric input and longer than 1 character as a name                                                                                   |   User’s input with the first letter  capitalized if name starts with a letter                                                                                                                                                                                                                                            |       PASS      |
|                Validation of user's input                |   User enters a letter or a word                                                                                                                            |   User's input in uppercase                                                                                                                                                                                                                                                                                               |       PASS      |
|                    Using main menu                  |   User selects one option from the main menu: 1 for checking the rules, 2 for starting the game, and 3 for exiting the game                                 |   If user selects option ‘1’: the rules are displayed, and the main menu appears again.   If user selects option ‘2’: the game starts.   If user selects option ‘3’: the game ends.                                                                                                                                       |       PASS      |
|                 Check input’s length                |   User enters a single character or a word with the same length as the hidden word                                                                          |   If user enters a character, tells if the letter is or isn’t in the word.   If user enters a word with the same  length, tells if the user’s word is or isn’t the same as the hidden word.   If user enters a word with a different length than the hidden word, a message is displayed of ‘INVALID INPUT’               |       PASS      |
|        Hangman’s stages display at every round      |   User enters a valid input. ( A letter or a word with the same length as the hidden word)                                                                  |   If user enters a correct input, number of tries stay the same.   If user enters an incorrect input, number of tries decreases by one, and appears an updated stage of the hangman. Until the number of tries equals ‘0’                                                                                                 |       PASS      |
|                     Play again                    |   User enters ‘Y’ or ’N’  for deciding if he wants to play a new game.                                                                                      |   If user enters ‘Y’  or ‘y’, a new game will start.   If user enters ’N’ or ’n', the game is ended.                                                                                                                                                                                                                      |       PASS      |
|                  Checking the rules                 |   User asks for help at any moment of the game, he needs to enter ‘1’ instead of a letter or a full word.                                                   |   Rules are shown and the game continues.                                                                                                                                                                                                                                                                                 |       PASS      |
|                   Exiting the game                 |   User decides to exit  the game at any moment, he needs to enter ‘3’ instead of a letter or a full word.                                                   |   The game ends with a message of goodbye to the user                                                                                                                                                                                                                                                                     |       PASS      |
|                  Restarting the game               |   User decides to restart the game at any moment, he needs to enter ‘2’ instead of a letter or a full word.                                                 |   The user will be asked if he wants to start a new game, if the user answers ‘Y’ or ‘y’, the game will start with a new word.                                                                                                                                                                                            |       PASS      |
|   Messages display at the beginning of every round  |   User needs to enter valid inputs for guessing the hidden word ( valid inputs: an alphabetic character or a word with the same length as the hidden word)  |   When user decides to play, will have on the terminal an update for each round: general instructions, number of tries left, length of the hidden word, used letters that aren’t in the hidden word, letters that are in the hidden word, incorrect words with the same length as the hidden word, stage of the hangman.  |       PASS      |

## Deployment

### Fork and Deploy with GitHub

### Deploy with Heroku

## Credit

* Table Generator with markdown style guide:

    https://www.tablesgenerator.com/markdown_tables#

### People

* Mentor support, guidance, and tips to improve my coding skills throughout the project:

    - Brian Macharia

### Python Library Dependecies and Packages

### Others

* Add color to the terminal:

    - https://stackabuse.com/how-to-print-colored-text-in-python/

* Checking code information (syntax and uses):

    - https://www.w3schools.com/python/ref_string_isalpha.asp
    
    - https://www.educative.io/edpresso/how-to-compare-two-strings-in-python

    - https://stackoverflow.com/questions/49463141/how-to-print-a-list-like-a-string

    - https://www.delftstack.com/howto/python/python-find-all-indexes-of-a-character-in-string/#:~:text=We%20can%20use%20the%20finditer,indexes%20where%20the%20pattern%20occurs.