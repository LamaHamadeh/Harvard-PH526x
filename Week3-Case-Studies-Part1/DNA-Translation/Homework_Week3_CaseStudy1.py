#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:46:13 2017

@author: lamahamadeh
"""

#A cipher is a secret code for a language. In this case study, we will explore 
#a cipher that is reported by contemporary Greek historians to have been used 
#by Julius Caesar to send secret messages to generals during times of war.

#The Caesar cipher shifts each letter of this message to another letter in the 
#alphabet, which is a fixed number of letters away from the original. 
#If our encryption key were 1, we would shift h to the next letter i, 
#i to the next letter j, and so on. If we reach the end of the alphabet, 
#which for us is the space character, we simply loop back to a. 
#To decode the message, we make a similar shift, except we move the same 
#number of steps backwards in the alphabet.

#----------------------------------------------------------------------------------------------------------------


# Exercise 1
#-----------

#TODO: Create a dictionary letters with keys consisting of the numbers from 0 
#to 26, and values consisting of the lowercase letters of the English alphabet,
# including the space ' ' at the end.

# Let's look at the lowercase letters.
import string
string.ascii_lowercase

# We will consider the alphabet to be these letters, along with a space.
alphabet = string.ascii_lowercase + " "

# create `letters` here!
letters = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i'
           , 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q'
           , 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y'
           , 25:'z', 26:' '}

#Another way is:

letters = {i:alphabet[i] for i in range(0,27)}
print(letters)

#------------------------------------------------------------------------------

# Exercise 2
#-----------

#alphabet and letters are already defined. Create a dictionary encoding with 
#keys being the characters in alphabet and values being numbers from 0-26, 
#shifted by an integer encryption_key=3. For example, the key a should have 
#value encryption_key, key b should have value encryption_key + 1, and so on. 
#If any result of this addition is less than 0 or greater than 26, you can 
#ensure the result remains within 0-26 using result % 27.





#------------------------------------------------------------------------------

# Exercise 3
#-----------








