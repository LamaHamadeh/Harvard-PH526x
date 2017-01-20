#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:26:48 2017

@author: lamahamadeh
"""

#First: Python-based implementation 
#------------------------------------
'''
source:
-------
Video 2.4.2: Examples Involving Randomness
Week 2 Overview/Python Libraries and Concepts Used in Research
Using python for research
Harvard
online course provided by edx.org
url: https://courses.edx.org/courses/course-v1:HarvardX+PH526x+3T2016/courseware/317ce880d7644d35840b1f734be76b06/391063d8f58242e892efafc9903b36e8/
'''
#roll a dice 100 times and plot a histogram of the outcomes
#meaning: a histogram that shows how frequent the numbers from 1 to 6 appeared in the 100 samples

import numpy as np
import random 
import matplotlib.pyplot as plt
import time

random.choice([1,2,3,4,5,6]) #this line throws the dice one time 

rolls = []              
              
for k in range(100):#we can try 1000, 10000000 times. We can notice that the histogram gets more flat when the number of rolling times increases.
    rolls.append(random.choice([1,2,3,4,5,6]))#in this case, after using for loop, we wre rolling the dice 100 times    
        
print(len(rolls))


#draw a histogram

plt.figure()
plt.hist(rolls, bins = np.linspace(0.5,6.5,7));
plt.show()

start_time = time.clock()
#This time we will roll 10 dice not jsut one
ys = []
for rep in range(100000):#By increasing the number of dice rolls for each dice the distrbution follows the central limit theorem
#The central limit theorem (CLT) states that the sum of a large number of random variables regardless of their distribution will
#approximately follow a normal distribution (or Gaussian distribution).
    y = 0
    for k in range (10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)

end_time = time.clock()

speed1 = end_time - start_time
print(speed1)#1.19823723963
   
print(len(ys)) #100
print(min(ys)) 
print(max(ys)) 

plt.figure()
plt.hist(ys); #the semicolon suppresses the output 
plt.show()

#------------------------------------------------------------------

#Second: NumPy random module implementation
#------------------------------------------
'''
source:
-------
Video 2.4.3: using the NumPy Random Module
Week 2 Overview/Python Libraries and Concepts Used in Research
Using python for research
Harvard
online course provided by edx.org
url: https://courses.edx.org/courses/course-v1:HarvardX+PH526x+3T2016/courseware/317ce880d7644d35840b1f734be76b06/391063d8f58242e892efafc9903b36e8/
'''
# We will repeate the previous example, but this time we will use Numpy


start_time = time.clock()

X= np.random.randint(1,7,(100000,10)) #generate random numbers between 1 and 6 in a 2D matrix where we have 100 rows and 10 columns
Y = np.sum(X, axis=1) #sum over all the columns (the length of Y =100)
#if you sum over all the columns, the length of the resulting list = the length of your rows
#if you sum over all the rows, the length of the resulting list = the length of your columns

end_time = time.clock()
speed2 = end_time - start_time
print(speed2)#0.0248949445651


plt.hist(Y)

#Generally using numpy is much faster than using standard python implementation. This is very important in scientific research.
#we can prove that by calculating the value of:
#speed1/speed2=1.19823723963/0.0248949445651=49.9
#and it is obviously can be seen taht using numpy is not only uses a less code but also much faster than the python-based
#implementation (with approximately 50 times faster in our case).
#ususally the coding speed value depends on your computer speed, so it doesn't have to hold the same value for everyone.
#You might get a different value
#------------------------------------------------------------------


