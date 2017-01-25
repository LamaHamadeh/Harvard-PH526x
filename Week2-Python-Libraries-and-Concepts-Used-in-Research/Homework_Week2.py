#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:27:28 2017

@author: lamahamadeh

*Still working on it*
"""


#Tic-tac-toe (or noughts and crosses) is a simple strategy game in which two players take turns placing a mark on a 3x3 board,
#attempting to make a row, column, or diagonal of three with their mark. In this homework, we will use the tools we've covered 
#in the past two weeks to create a tic-tac-toe simulator, and evaluate basic winning strategies.

#----------------------------------------------------------------------------------------------------------------


# Exercise 1
#-----------

#For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3. Make a function create_board() that creates such 
#a board, with values of integers 0. 

import numpy as np

def create_board():
    return np.zeros ((3,3))

#Call create_board(), and store this as board.

board = create_board()              

#------------------------------------------------------------------------------

# Exercise 2
#-----------

#Players 1 and 2 will take turns changing values of this array from a 0 to a 1 or 2, indicating the number of the player who places there. 
#Create a function place(board, player, position) with player being the current player (an integer 1 or 2), and position a tuple of length 
#2 specifying a desired location to place their marker. Only allow the current player to place a piece on the board (change the board position 
#to their number) if that position is empty (zero).

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
    

#Use create_board() to store a board as board, and use place to have Player 1 place a piece on spot (0, 0).                                

board = create_board() 
place(board , 1 , (0,0))

#print (board)               
                 
#------------------------------------------------------------------------------

# Exercise 3
#-----------

#Create a function possibilities(board) that returns a list of all positions (tuples) on the board that are not 
#occupied (0). (Hint: numpy.where is a handy function that returns a list of indexes that meet a condition.)

def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))



#board is already defined from previous exercises. Call possibilities(board) to see what it returns!

print(possibilities(board))

#------------------------------------------------------------------------------

# Exercise 4
#-----------

#Create a function random_place(board, player) that places a marker for the current player at random 
#among all the available positions (those currently set to 0).

import random 

def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selection = random.choice(selections)
        place(board, player, selection)
    return board
  
                         
                               
#board is already defined from previous exercises. Call random_place(board, player) to place a random 
#marker for Player 2, and store this as board to update its value.

random_place(board, 2)

#------------------------------------------------------------------------------

# Exercise 5
#-----------

#board is already defined from previous exercises. Use random_place(board, player) to place three pieces 
#on board each for players 1 and 2.

board = create_board()
for i in range(3):
    for player in [1, 2]:
        random_place(board, player)                                                                   
                                                                   
#Print board to see your result

print(board)

#------------------------------------------------------------------------------

#Exercise 6
#-----------

#Now that players may place their pieces, how will they know they've won? Make a function row_win(board, player) 
#that takes the player (integer), and determines if any row consists of only their marker. 
#Have it return True of this condition is met, and False otherwise.

def check_row(row, player):
    for marker in row:
        if marker != player:
            return False
    return True

def row_win(board, player):
    for row in board:
        if check_row(row, player):
            return True
    return False                                                                                        
                                                                                                 
#board is already defined from previous exercises. Call row_win to check if Player 1 has a complete row.

row_win(board, 1)
#------------------------------------------------------------------------------

#Exercise 7
#-----------

#Create a similar function col_win(board, player) that takes the player (integer), 
#and determines if any column consists of only their marker. Have it return True if this condition is met, 
#and False otherwise.
        
def col_win(board, player):
    for row in board.T:
        if check_row(row, player):
            return True
    return False
                                  
                                  
#board is already defined from previous exercises. Call col_win to check if Player 1 has a complete column.

col_win(board, 1)
#------------------------------------------------------------------------------

#Exercise 8
#-----------

#Finally, create a function diag_win(board, player) that tests if either diagonal of the board 
#consists of only their marker. Have it return True if this condition is met, and False otherwise.

def diag_win(board, player):
    main_diag = board.diagonal()
    anti_diag = np.flipud(board).diagonal()[::-1]
    return check_row(main_diag, player) or check_row(anti_diag, player)                                    


#board is already defined from previous exercises. Call diag_win to check if Player 1 has a complete diagonal.

diag_win(board, 1)

#------------------------------------------------------------------------------

#Exercise 9
#-----------




#------------------------------------------------------------------------------
