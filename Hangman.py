"""
Script: WordGame
Author: Andres R. Gonzalez Poveda
"""
import random

# List of words to be played
word_list = ("processes", "interpreter", "fundamental")
# game_word: Random selection of a word for the game.
game_word = random.choice(word_list)
game_word_len = len(game_word)
attempts_qtty = game_word_len + 7
ltrs_positions = dict()
str_line = "##############################################"


def word_converter(game_word):
    """ Method creates three different variables
    with the word that is going to be played."""
    gw_dict = {}
    gw_set = set()
    user_layout = {}
    ltt_position = 0

    for letter in game_word:
        # gw_dict: is a dictionary variable of the game_word with
        # the position of the letter as key value.
        gw_dict[ltt_position] = letter
        # user_layout: is a list variable with the structure
        # of the game_word to be replaced later by the
        # letter selected by the user (game_letter).
        user_layout[ltt_position] = "_"
        # gw_set: is a set variable, contains the unique letters of the game_word
        gw_set.add(letter)
        ltt_position += 1

    return gw_dict, user_layout, gw_set


gw_dict, user_layout, gw_set = word_converter(game_word)


def wl_position(game_letter):
    """ Method receives the letter selected by the user (game_letter)
    and checks the position(s) of this letter in the word that was
    randomly selected (game_word) for the game. """
    pst_counter = 0
    for item in gw_dict.values():
        if item == game_letter:
            ltrs_positions[pst_counter] = item
        pst_counter += 1

    return ltrs_positions


def ltt_exist(game_letter, gw_set):
    """ Method checks if the letter selected (game_letter) by the
    user exists in the word selected for the game (game_word).
    Returns informative string and boolean value for further iterations."""
    if game_letter in gw_set:
        print(str_line)
        print('the letter: "' + game_letter + '" is in the list')
        return True
    else:
        print(str_line)
        print('the letter: "' + game_letter + '" is not in the list')
        return False


def print_info(str_line, succs_attempts, error_counter, attempts_left):
    """ Method returns informative strings to the user of
    the current status of the game."""
    print(str_line)
    print("For this word you have " + str(attempts_qtty) + " attempts to win.")
    print("You have " + str(succs_attempts) + " successful attempts.")
    print("You have made " + str(error_counter) + " errors.")
    print("You have " + str(attempts_left) + " attempts left.")
    print(str_line)


def word_constructor(ltrs_qtty, ltrs_positions, user_layout):
    """ Method generate the current state of the game, by receiving the
    list of postions of each letter (game_letter) and replacing this letters
    in user_layout to return a string with the current progress."""
    # For loop creates a dictionary variable with the current
    # state of the word being assembled.
    for i in range(0, ltrs_qtty):
        for position in ltrs_positions:
            user_layout[position] = ltrs_positions[position]

    current_layout_str = ""
    # For loop creates the current progress of the game
    # to be displayed later with string type format.
    for letter in user_layout.values():
        current_layout_str += letter

    return current_layout_str


def check_win(current_layout_str):
    """ Method checks the current status of the word being
    played by the user, if it is complete, informs the user has
    won and ends the game. """
    if game_word == current_layout_str:
        print("You have won!!!")
        print("The word was: ", game_word)
        exit()


def game_operator():
    """ Method to execute the previous methods through loops and
    run the game. """
    error_counter = 0
    succs_attempts = 0
    print("For this word you have " + str(attempts_qtty) + " attempts to win.")

    # For loop of the methods according to the number of possible attempts for the user.
    for i in range(0, attempts_qtty):
        # In current_attempts variable was necessary a manual fix (+ 1),
        # while for an unknown reason the succs_attempts or the error_counter
        # variables at the first iteration of the if loop does not add up
        # the new value to itself.
        current_attempts = error_counter + succs_attempts + 1
        attempts_left = attempts_qtty - current_attempts

        game_letter = input("Enter a letter: ").lower()

        ltrs_positions = wl_position(game_letter)
        ltrs_qtty = len(ltrs_positions)

        # If loop with function ltt_exist, if game_letter exist runs word_constructor()
        # and check if the user has already won, and counts the successful attempts.
        # Else loop, if game_letter do not exist runs word_constructor() and counts the
        # errors attempts
        if ltt_exist(game_letter, gw_set):
            succs_attempts += 1

            current_layout_str = word_constructor(ltrs_qtty, ltrs_positions, user_layout)

            print("Current progress:")
            print(current_layout_str)

            print_info(str_line, succs_attempts, error_counter, attempts_left)

            check_win(current_layout_str)
        else:
            error_counter += 1

            print_info(str_line, succs_attempts, error_counter, attempts_left)
            current_layout_str = word_constructor(ltrs_qtty, ltrs_positions, user_layout)

            print("Current progress:")
            print(current_layout_str)
            print(str_line)

    # When the for loop ends the user is out of available attempts
    # and the game word is exited.
    print(str_line)
    print("You are out of attempts! GameOver, keep trying...")
    print(str_line)
    exit()


game_operator()
