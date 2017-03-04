#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 22:41:26 2017

@author: lamahamadeh
"""

'''
Case Study about Language Processing
'''

#counting words
#---------------

text = "This is a test text. We're keping this text short to keep things manageable." #test text

#Using loops
#-----------

def count_words(text):
    '''count the number of times each word occurs in text (str). 
    Return dictionary where keys are unique words and values are 
    word counts. skip punctuations'''
    text = text.lower() #lowercase for the counting letters so the function can cont the same words whether it's capatilised or not
    skips = [".", ",", ";", ":", "'", '"'] #skipping all the punctuations to not be counted with the words that come bfore them
    for ch in skips:
        text = text.replace(ch,"")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts: #known word case
            word_counts[word] += 1
        else:
            word_counts[word] = 1 #unknown word case
    return word_counts

print(count_words(text))
print(len(count_words("This comprehension check is to check for comprehension.")))#first quiz question
#------------------------------------------------------------------------------
 
#using collections module
#-------------------------

from collections import Counter

def count_words_fast(text):
    '''count the number of times each word occurs in text (str). 
    Return dictionary where keys are unique words and values are 
    word counts. skip punctuations'''
    text = text.lower() #lowercase for the counting letters so the function can cont the same words whether it's capatilised or not
    skips = [".", ",", ";", ":", "'", '"'] #skipping all the punctuations to not be counted with the words that come bfore them
    for ch in skips:
        text = text.replace(ch,"")
    word_counts = Counter(text.split(" "))
    return word_counts

print(count_words_fast)

print(count_words(text)==count_words_fast(text))
print(count_words(text) is count_words_fast(text))#second quiz question

#------------------------------------------------------------------------------

#read a book
#-------------
'''
def read_book(title_path):
    '''
    Read a book and return it as a string
    '''
    with open(title_path, "r", encoding= "utf8") as current_file:#utf8 is a character encoder 
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text
        

text = read_book(' ')#read a book from its path

print(len(text))#number of charatcers in the book

#if there is a famous/wanted line in the book we can use the 'find' method to find it
ind = text.find(" write the famous line")
print(ind)#print the index number of the famous/wanted sentence
sample_text = text[ind : ind + 1000]#slice the paragraph that contains the famous line
print(sample_text)#print the whole paragraph
'''  
#------------------------------------------------------------------------------
