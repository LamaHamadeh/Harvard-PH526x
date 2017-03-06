# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 13:34:51 2017

@author: ADB3HAMADL
"""


'''
==============================
Case Study 2 - 
==============================
'''

#In this case study, we will find and plot the distribution of word frequencies for each translation of Hamlet. 
#Perhaps the distribution of word frequencies of Hamlet depends on the translation --- let's find out!

#For these exercises, functions count_words_fast, read_book, and word_stats are already defined as in the Case 2 Videos (Videos 3.2.x).
#----------------------------------------------------------------------------------------------------------------

#Define functions
#------------------
from collections import Counter

def count_words_fast(text):
    """count the number of times each word occurs in text (str). 
    Return dictionary where keys are unique words and values are 
    word counts. skip punctuations"""
    text = text.lower() #lowercase for the counting letters so the function can cont the same words whether it's capatilised or not
    skips = [".", ",", ";", ":", "'", '"'] #skipping all the punctuations to not be counted with the words that come bfore them
    for ch in skips:
        text = text.replace(ch,"")
    word_counts = Counter(text.split(" "))
    return word_counts

#------------------
def read_book(title_path):
    """Read a book and return it as a string"""
    with open(title_path, "r") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text

#------------------
def word_stats(word_counts):
   """return the number of unique words and word frequencies"""
   num_unique = len(word_counts) #calculate the number of unique words in the text
   counts = word_counts.values() #calculate the frequency of each word in the text
   return(num_unique,counts)

#----------------------------------------------------------------------------------------------------------------

# Exercise 1
#-----------

#TODO: Write a function word_count_distribution(text) that takes a book string and returns a dictionary with items 
#corresponding to the count of times a collection of words appears in the translation, and values corresponding to 
#the number of number of words that appear with that frequency.


#TODO: First use count_words_fast(text) to create a dictionary called word_counts with unique words in the dictionary 
#as keys and their frequency in the book as values.


#TODO: Next, create and return a new dictionary count_distribution with unique values from word_counts as keys and their 
#frequency as values. For example, 'you are what you eat' contains three words that occur once and one word that occurs twice, 
#so word_count_distribution('you are what you eat') should return a dictionary {1:3, 2:1}.


#TODO: 'Romeo and Juliet' is preloaded as text. Call word_count_distribution(text), and save the result as distribution.


#------------------------------------------------------------------------------

# Exercise 2
#-----------

#TODO: 

#------------------------------------------------------------------------------
