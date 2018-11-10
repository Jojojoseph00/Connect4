###
#Python game: Connect4
#
#Copyright (c) Youssef El-Moukhtar @Owl-ProjX
#
###
-*- coding: utf-8 -*-

import numpy as np


# Creating the game board:
game_board = np.zeros((r, c))



#Class game represeting a game:
class Game:
    mat = None # this represents the board matrix
    rows = 0 # this represents the number of rows of the board
    cols = 0 # this represents the number of columns of the board
    turn = 0 # this represents whose turn it is (1 for player 1, 2 for player 2)
    wins = 0 # this represents the number of consecutive disks you need to force
             # in order to win



#Game instance:
my_game = Game()



def check_victory(game):
    pass
    # This function's role is to check if a victory situation has been reached
    # It will take a game input and return:
    # 0 if no winning or draw situation is present for this game
    # 1 if player 1 wins
    # 2 if player 2 win
    # 3 if it is a draw



def apply_move(game,col,pop):
    pass
    # This function’s role is to apply a certain move to a game.
    # It will take a game as input, as well as a column value col and a boolean
    # value pop that will represent the move.
    # It returns a game with an updated board according to that move



def check_move(game,col,pop):
    pass
    # This function's role is to check if a certain move is valid for a certain
    # game. It will take a game as input, as well as a column value col and a
    # boolean value pop that will represent the move.
    # It returns a boolean value False if the move is impossible and True if it
    # is possible



def computer_move(game,level):
    pass
    # This function's role is to ask for the computer to make a move for a
    # certain game. It will take a game as input, as well as a level that will
    # represent the level of difficulty of the computer. It will return a
    # column value and a boolean value (for the pop) that represents the move
    # chosen by the computer



def display_board(game):
    pass
    # The function's role is to display the board in the console. It takes
    # a game input and does not return anything.



def menu():
    pass
    # This function's role is to handle the menu interface with the user via
    # the console. It is basically the director fucntion that will interact
    # with the user and distribute the work to all other function. It should
    # be the main fucntion that is called in the script it takes no input and
    # does not output anything


def display_board():
    pass



# comment here
