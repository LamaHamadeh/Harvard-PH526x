#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 22:06:22 2017

@author: lamahamadeh
"""

# This code works for Python 2.7

import random
#generate the tic-tac-toe board 
board = [0,1,2,3,4,5,6,7,8]
#draw the board
def showboard():
    print (str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
    print ('----------')
    print (str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
    print ('----------')
    print (str(board[6])+" | "+str(board[7])+" | "+str(board[8]))
    
    
def CheckLine(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True
    
    
def CheckAll(char):
    #winner rows
    if CheckLine(char, 0, 1, 2):
        return True
    if CheckLine(char, 3, 4, 5):
        return True
    if CheckLine(char, 6, 7, 8):
        return True
    #winner columns 
    if CheckLine(char, 2, 4, 6):
        return True
    if CheckLine(char, 0, 3, 6):
        return True
    if CheckLine(char, 1, 4, 7):
        return True
    #winner diagonals
    if CheckLine(char, 2, 5, 8):
        return True
    if CheckLine(char, 0, 4, 8):
        return True
    
    
while True:
    
    number = raw_input("Select a number: ")
    number = int(number)
    
    if board[number] != 'x' and board[number] != 'o':
        board[number] = 'x'
        
        if CheckAll('x') == True:
            print ("X Wins!")
            break;
            
        while True:
            
            number2 = random.randint(0,8)
            
            if board[number2] != 'x' and board[number2] != 'o':
                board[number2] = 'o'
                showboard()
                
                if CheckAll('o') == True:
                    print ("O Wins!")
                    break;
                    
                break;
    else:
        
        print ("Spot Taken... Try again.")
        break;