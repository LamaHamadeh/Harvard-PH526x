#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:06:22 2017

@author: lamahamadeh
"""

# ***This code works for Python 2.7, but not for Python 3.5!***

#import random module for generating random posiitons for the other player
#-------------------------------------------------------------------------
import random

#------------------------------------------------------------------------------

#Define the indicies of the tic-tac-toe board positions
#------------------------------------------------------

board = [0,1,2,3,4,5,6,7,8]

#------------------------------------------------------------------------------

#draw the board
#---------------

def showboard():
    print (str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
    print ('----------')
    print (str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
    print ('----------')
    print (str(board[6])+" | "+str(board[7])+" | "+str(board[8]))
    
#------------------------------------------------------------------------------

#Define a function where it returns 'True' if any of the game possibilities
#consists of the same marker (i.e., same player). This function helps in
#defining who's the winner
#-----------------------------------

def CheckLine(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True
#------------------------------------------------------------------------------

    
#Defining the winning possibilities
#-----------------------------------
 
def CheckAll(char):
    #winning rows
    if CheckLine(char, 0, 1, 2):
        return True
    if CheckLine(char, 3, 4, 5):
        return True
    if CheckLine(char, 6, 7, 8):
        return True
    #winning columns 
    if CheckLine(char, 0, 3, 6):
        return True
    if CheckLine(char, 1, 4, 7):
        return True
    if CheckLine(char, 2, 5, 9):
        return True  
    #winning diagonals
    if CheckLine(char, 2, 4, 6):
        return True
    if CheckLine(char, 0, 4, 8):
        return True
#------------------------------------------------------------------------------
    
#The game Code
#--------------

#NOTE
#-----
#While loops, like the ForLoop, are used for repeating sections of code - 
#but unlike a for loop, the while loop will not run n times, but until a 
#defined condition is met. As the for loop in Python is so powerful, while is 
#rarely used, except in cases where a user's input is required.


while True: # Having True as a condition ensures that the following code runs  
#until it's broken by one of the three conditions: X wins, O Wins or spot is 
#taken. 

#input a number to fill in one of the board position
#---------------------------------------------------    
    number = raw_input("Select a number: ")
    number = int(number)

#check, if the position that is chosen in the previous step is not occupied by
#either x or o, then put x in it
#---------------------------------------------------   
    if board[number] != 'x' and board[number] != 'o':
        board[number] = 'x'

#keep checking when all the posiiotn have the same marker (x) until the first
# player is the winner!
#-----------------------------------------------------        
        if CheckAll('x') == True:
            print ("X Wins!")
            break;#This break belongs to having the first player 
                    #is the winner
       
        #we need another while loop to generate random input for the second
        #player. This loop is broken when 'if CheckAll('o') == True' is met.
        #------------------------------------
        while True:
            
            number2 = random.randint(0,8) #generate random numbers from 0 to 8
            
            #check the availability of the position
            #--------------------------------------                        
            if board[number2] != 'x' and board[number2] != 'o':
                board[number2] = 'o'
                showboard()
                
                #if the three posititions have o, then the second player is the
                #winner
                #-----------------------------------
                if CheckAll('o') == True:
                    print ("O Wins!")
                    break; #This break belongs to having the second player 
                    #is the winner
                    
                break; #belongs to checking the availibility for the second player
                #' if board[number2] != 'x' and board[number2] != 'o':'
                    
    else: #if the input is taken by another player (this can be checked by
    #board[number]!='x' and board[number]!='o'), then do the following line
        print ("Spot Taken... Try again.")
        break; #belongs to the first 'if'
#------------------------------------------------------------------------------
