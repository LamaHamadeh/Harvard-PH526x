# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 09:34:17 2017

@author: lamahamadeh
"""

'''
Case Study about an introduction to kNN classifiction
'''

#Finding the Euclidean Distance Between Two Points
#---------------------------------------------------

import numpy as np

def distance(p1,p2):
    "find the distance betweeen points p1 and p2"
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))


p1 = np.array([1,1])
p2 = np.array([4,4])
    
print distance(p1,p2)

#------------------------------------------------------------------------------

#Majority Vote
#-------------

import random

def majority_vote(votes):
    "Return the most common element in votes"
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    #items method
    winners = []
    max_counts = max(vote_counts.values()) #ask Python about the frequency the most appearing value has
    for vote, count in vote_counts.items(): #this returns a tuple of (vote,count)
        if count == max_counts:
            winners.append(vote)
        
    return random.choice(winners) #in case of a tie situation, Python picks a random candidate (element) and returns it.

votes = [1, 2, 3, 1, 2 ,3 ,3 ,3 ,3, 2, 2, 2]
winner = majority_vote(votes)
print winner #it can be seen after runnign the code several times that thsi methods picks one of the candidates
#and return it randomly.

#another method
#--------------
import scipy.stats as ss

def majority_vote_short(votes):
    "Return the most common element in votes "
    mode , count = ss.mstats.mode(votes)  
    return mode

votes = [1, 2, 3, 1, 2 ,3 ,3 ,3 ,3]
winner_short = majority_vote_short(votes)
print winner_short # it can be seen after runnign the code several times that this method always 
#returns number 3 as the most common candidate and forgets about the other one: 2

#------------------------------------------------------------------------------

#Finding Nearest Neighbors
#--------------------------



#------------------------------------------------------------------------------




