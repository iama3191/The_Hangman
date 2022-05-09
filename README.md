# The Hangman

![Responsive Design](assets/responsive.png)

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
* [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
* [Testing](#testing)
    * [User Stories](#user-stories)
    * [Functionality](#functionality)
* [Deployment](#deployment)
    * [How to clone the GitHub repository](#how-to-clone-the-github-repository)
    * [How to fork the GitHub repository](#how-to-fork-the-github-repository)
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

* What a user may want:

    - Clear instructions to play the game

    - Clear messages on how many attempts he has, what letters he has used, warning messages when something went wrong, updated hangman stage.

    - The possibility to restart the game at any time of the game.

    - The possibility to check the rules at any time of the game.

    - The possibility to exit the game at any time of the game.
    
    - The possibility to resume the game if he doesn't want to exit or restart the game.

    - That the words in the game belong to a specific category.
    
    - After each round, he can decide to play a new round or simply exit the game.

* As a developer what I expect

    - The user finds an entertaining and easy game to play.

    - Well-commented code for easy maintenance.

### Structure

The game has a series of logical steps for easy interaction with the program. The user is accompanied at all times with messages so that he understands what input he has to enter and so that he can make a decision at any time without waiting for the end of the game. At the same time, for every action the user performs, he will receive a response, either negative or positive.

### Skeleton

The game is built to follow a slightly more user-friendly visual pattern, there are certain line designs at each drastic change of the game: At the start of the game, at the end of the game, at each attempt and when showing the rules. In addition, new lines were used at the end of each message so that the screen was not overloaded. 

### Surface

Three colors in addition to the default white were used to create an alert to the user as to the level of importance of what is happening in the game.
Yellow is used to draw the user's attention to how many chances he has after each letter is entered, red was used to warn him that the entered data is invalid or incorrect (not part of the secret word). And green is used to tell the user that he is succeeding.

## Features

### Current Features

- Main menu with three options: (1) Check the rules, (2) Start the game and (3) Quit the game

- List with letters entered by the user in alphabetical order: incorrect letters (do not belong to the secret word), correct letters (belong to the secret word), used letters (all valid options entered).

- The state of the hangman is updated every time the user loses a chance, therefore it warns the user of the danger of losing.

- At any point in the game, the user can choose between '1' check rules, '2' restart the game, and '3' exit the game. Choosing '1', the rules are displayed and immediately the game continues without any changes, choosing '2', the user is asked if he wants a new game, saying 'y' or 'Y', the new one is started, if he chooses 'n' or 'N', the game will resume. While choosing '3', the user will be asked if he's really sure to exit the game.

### Future Features

- Create and add a scoring system. The number of attempts left are the points that are added to the user.

- Create a table of players based on the score, the table would show: position in the game, username and points collected.

- Create several categories for the user to decide what type of word he would like to guess.

## Technologies Used

### Languages Used

* [Python 3.8.11](https://www.python.org/)

### Frameworks, Libraries and Programs Used

* [Git](https://git-scm.com): Was used for version control by using the Gitpod terminal to commit to Git and Push to GitHub.

* [GitHub](https://github.com): Was used as the repository for the project's code after being pushed from Git.

* [Heroku](https://www.heroku.com): Was used to deploy the application and provides an environment in which the code can execute.

## Testing

### User Stories

The game uses the command line interface, and it isn't very user friendly for a human end-user. Because of that, the user stories where tested to prioritize a better UI (User Interface).

|   Reference   |   Description                                                                                                                                                                                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   US01        |   As a user, I want to check a main menu with multiple choices for deciding if I want to play, check the rules or exit the game.                                                                                                                                                     |
|   Validation  |   The only way to start the game is if the user enters number ‘2’, the rules are displayed entering number ‘1’ and if user enters number ‘3’, the game won’t start.                                                                                                                  |
|   US02        |   As a user, I want to understand how many tries I have, what letters I’ve used on every opportunity before I guess the secret word or the hangman is completed                                                                                                                      |
|   Validation  |   From the beginning of the game and for each try, the user can see the number of tries left, the number of letters of the secret word, the letters that he has already used  (incorrect letters, correct letters and used letters), the words he has tried and the hangman stage.   |
|   US03        |   As a user, I want to check the rules without ending the current game.                                                                                                                                                                                                              |
|   Validation  |   The user can check the rules at any point of the game, he only needs to enter number ‘1’, the rules will be displayed and then the game can continue.                                                                                                                              |
|   US04        |   As a user, I want to restart or exit the game at any point and I don’t want to wait until the end of it.                                                                                                                                                                           |
|   Validation  |   The user can enter number ‘2’ for restarting the game or number ‘3’ for exiting the game at any point. He will be asked if he is sure of his selection, if he is, the program will proceed. In case, he isn’t, he can always resume the game.                                      |
|   US05        |   As a user, if I don’t guess the word, I would like to know the right answer.                                                                                                                                                                                                       |
|   Validation  |   If the user doesn’t get the word, a message with the hidden word is shown.                                                                                                                                                                                                         |
|   US05        |   As a user, I don’t want to decrease my number of tries if I make a typo (white space, symbol, or number)                                                                                                                                                                           |
|   Validation  |   All user’s inputs are verified to decrease the penalizations for minor errors. The user is penalized if the letter is incorrect and if he tries to enter an incorrect word with the same length as the hidden word.                                                                |
|   US06        |   As a user, I want to have the opportunity to start a new game after 8 tries ( = round).                                                                                                                                                                                            |
|   Validation  |   After each round, no matter if the user guesses the hidden word or doesn’t , he will be asked if he would like to play a new game. If the answer is ‘y’, a new game will start.                                                                                                    |


### Functionality

|   Test Label                                        |   Test Action                                                                                                                                               |   Expected Outcome                                                                                                                                                                                                                                                                                                        |   Test Outcome  |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|
|   Validate user’s name                              |   User enters an alphanumeric input and longer than 1 character as a name                                                                                   |   User’s input with the first letter  capitalized if name starts with a letter                                                                                                                                                                                                                                            |   PASS          |
|   Validate user's input                             |   User enters a letter or a word                                                                                                                            |   User's input in uppercase                                                                                                                                                                                                                                                                                               |   PASS          |
|   Using main menu                                   |   User selects one option from the main menu: 1 for checking the rules, 2 for starting the game, and 3 for exiting the game                                 |   If user selects option ‘1’: the rules are displayed, and the main menu appears again.   If user selects option ‘2’: the game starts.   If user selects option ‘3’: the exit_game function is call                                                                                                                       |   PASS          |
|   Check input’s length                              |   User enters a single character or a word with the same length as the hidden word                                                                          |   If user enters a character, tells if the letter is or isn’t in the word.   If user enters a word with the same  length, tells if the user’s word is or isn’t the same as the hidden word.   If user enters a word with a different length than the hidden word, a message is displayed of ‘INVALID INPUT’               |   PASS          |
|   Hangman’s stages display at every round           |   User enters a valid input. ( A letter or a word with the same length as the hidden word)                                                                  |   If user enters a correct input, number of tries stay the same.   If user enters an incorrect input, number of tries decreases by one, and appears an updated stage of the hangman. Until the number of tries equals ‘0’                                                                                                 |   PASS          |
|   Play again                                        |   User enters ‘Y’ or ’N’  for deciding if he wants to play a new game.                                                                                      |   If user enters ‘Y’  or ‘y’, a new game will start.   If user enters ’N’ or ’n', the game is ended.                                                                                                                                                                                                                      |   PASS          |
|   Checking the rules                                |   User asks for help at any moment of the game, he needs to enter ‘1’ instead of a letter or a full word.                                                   |   Rules are shown and the game continues.                                                                                                                                                                                                                                                                                 |   PASS          |
|   Exiting the game                                  |   User decides to exit  the game at any moment, he needs to enter ‘3’ instead of a letter or a full word.                                                   |   The user will be asked if he really wants to exit the game. If he enters ‘y’ or ‘Y’, a message will thank the user and the game is over. If the answer is ’n’ or ’N’, the game will continue.                                                                                                                           |   PASS          |
|   Restarting the game                               |   User decides to restart the game at any moment, he needs to enter ‘2’ instead of a letter or a full word.                                                 |   The user will be asked if he wants to start a new game, if the user answers ‘Y’ or ‘y’, the game will start with a new word.                                                                                                                                                                                            |   PASS          |
|   Messages display at the beginning of every round  |   User needs to enter valid inputs for guessing the hidden word ( valid inputs: an alphabetic character or a word with the same length as the hidden word)  |   When user decides to play, will have on the terminal an update for each round: general instructions, number of tries left, length of the hidden word, used letters that aren’t in the hidden word, letters that are in the hidden word, incorrect words with the same length as the hidden word, stage of the hangman.  |   PASS          |
|   New game                                          |   After each round, no matter the result ( if user wins or loses), he needs to answer if he wants to play a new game with ‘Y’ or ’N'                        |   If the user answers ‘Y’, a new game is staring; if he declines, the game will end.                                                                                                                                                                                                                                      |   PASS          |
## Deployment

### How to clone the GitHub repository

1. Go to the https://github.com/iama3191/hangman to access the repository on GitHub.

2. Click on the 'Code' button which will bring a dropdown box.

3. Click the HTTPS and copy the link.

4. Open Gitbash terminal.

5. Change the current working directory to where you want the cloned directory to be.

6. Type `git clone`, and then paste the URL you copied earlier, hit Enter to start the cloning process.

7. Any changes made to the local clone can be pushed back to the repository using the following steps:

        a. Update the code as needed.
        b. Go to the terminal and type git add . (or other file_name')
        c. Type git commit -m "brief description of the change"
        d. Type git push

### How to fork the GitHub repository

1. Go to the website's repository on GitHub: https://github.com/iama3191/hangman

2. Go to the 'Fork' button on the right side of the screen and click.

3. Now you have a copy of the repository into your own GitHub account to make changes without affecting the original repository.


### Deploy with Heroku

The deployments are donde manually from the terminal.

**If you are creating a new deployment/app**

- Run the command `heroku login -i ` and login with email and password when prompted. Then run the command `heroku create your_app_name_here` to create a new app, replacing `your_app_name_here` with the name you want to give to your app. This will create a new Heroku app and link it to your Gitpod terminal. You can access the app via the Heroku dashboard and set up your config vars.

**If you already have an app created which uses automatic deploys.**

- Run the command `heroku login -i` and login with the email and password when prompted. Then run the following command: `heroku git:remote -a your_app_name_here` and replace `your_app_name_here` with the name of your Heroku app. This will link the app to your Gitpod terminal.

Once you have followed the appropriate step above, your Heroku app will be linked to your workspace.

**HOW TO DEPLOY**

After linking your app to your workspace with one of the above steps, you can then deploy new versions of the app by running the command `git push heroku main` and your app will be deployed to Heroku.


## Credit

* Table Generator with markdown style guide:

    https://www.tablesgenerator.com/markdown_tables#

### People

* Mentor support, guidance, and tips to improve my coding skills throughout the project:

    - Brian Macharia


### Others

* Add color to the terminal:

    - https://stackabuse.com/how-to-print-colored-text-in-python/

* Checking code information (syntax and uses):

    - https://www.w3schools.com/python/ref_string_isalpha.asp
    
    - https://www.educative.io/edpresso/how-to-compare-two-strings-in-python

    - https://stackoverflow.com/questions/49463141/how-to-print-a-list-like-a-string

    - https://www.delftstack.com/howto/python/python-find-all-indexes-of-a-character-in-string/#:~:text=We%20can%20use%20the%20finditer,indexes%20where%20the%20pattern%20occurs.