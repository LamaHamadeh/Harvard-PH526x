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
    """count the number of times each word occurs in text (str). 
    Return dictionary where keys are unique words and values are 
    word counts. skip punctuations"""
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
    """count the number of times each word occurs in text (str). 
    Return dictionary where keys are unique words and values are 
    word counts. skip punctuations"""
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

def read_book(title_path):
    """Read a book and return it as a string"""
    with open(title_path, "r", encoding= "utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text
        

text = read_book('/Users/lamahamadeh/Desktop/Introduction.txt.rtf')#read a book from its path

print(len(text))#number of charatcers in the book

#if there is a famous/wanted line in the book we can use the 'find' method to find it
ind = text.find("The purpose of this chapter")
print(ind)#print the index number of the famous/wanted sentence
sample_text = text[ind : ind + 1000]#slice the paragraph that contains the famous line
print(sample_text)#print the whole chosen paragraph
 

#------------------------------------------------------------------------------

#Counting the number of unique words
#------------------------------------

def word_stats(word_counts):
   """return the number of unique words and word frequencies"""
   num_unique = len(word_counts) #calculate the number of unique words in the text
   counts = word_counts.values() #calculate the frequency of each word in the text
   return(num_unique,counts)
    
    
text = read_book('/Users/lamahamadeh/Desktop/Introduction.txt.rtf')

word_counts = count_words(text)

(num_unique, counts) = word_stats(word_counts)

print(num_unique) #print the number of unique number of words in the text
print(sum(counts)) #print the total number of words in the text

#------------------------------------------------------------------------------

#Reading multiple files
#-----------------------
 
    
import os #to read directories

book_dir = "./books" #tells us how many directories in the book directory

import pandas as pd

'''
Pandas example of how to create a dataframe:
--------------------------------------------
import pandas as pd

table = pd.DataFrame(coloums = ("name" , "age"))
table.loc[1] = "James", 22
table.loc[2] = "Jess", 32

print(table)
'''

stats = pd.DataFrame(columns = ("language" , "author" , "tilte" , "lenght" , "unique")) #this creates an empty dataframe 
#with empty table elements with 5 columns

#To put data in the table
title_num =1
for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" language + "/" + author):
            inputfile = book_dir + "/" language + "/" + author + "/" title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num ] = language , author.capilatize(), title.replace(".txt", " ") , sum(counts) , num_unique
            title_num += 1
            
print(stats) #print the created dataframe
print(stats.head()) #print the top 5 lines
print(stats.tail()) #print the last 5 lines

print(stats.length) #to extractm a specific column from the dtatframe
print(stats.unique)

stats[stats.language == "English"] #print the number of entries for language English
#------------------------------------------------------------------------------

#Plotting Book Statistics
#-------------------------

import matplotlib.pyplot as plt

plt.plot(stats.length, stats.unique, "bo")
plt.loglog(stats.length, stats.unique, "bo") #it is a straight line which suggest data modelling strategies that we might use

plt.figure(figsize = (10,10))

subset = stats[stats.language == "English"] #extract a subset that has only the rows with English Language
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "crimson")

subset = stats[stats.language == "French"] #extract a subset that has only the rows with French Language
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "orange")

subset = stats[stats.language == "German"] #extract a subset that has only the rows with German Language
plt.loglog(subset.length, subset.unique, "o", label = "English", color = "forestgreen")

plt.legend()
plt.xlabel("Book Length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plot.pdf")

#------------------------------------------------------------------------------


