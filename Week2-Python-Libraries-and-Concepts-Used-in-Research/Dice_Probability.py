#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:26:48 2017

@author: lamahamadeh

source:
-------
Video 2.4.2: Examples Involving Randomness
Week 2 Overview/Python Libraries and Concepts Used in Research
Using python for research
Harvard
online course provided by edx.org
url: https://courses.edx.org/courses/course-v1:HarvardX+PH526x+3T2016/courseware/317ce880d7644d35840b1f734be76b06/391063d8f58242e892efafc9903b36e8/
"""


#roll a dice 100 times and plot a histogram of the outcomes
#meaning: a histogram that shows how frequent the numbers from 1 to 6 appeared in the 100 samples

import numpy as np
import random 
import matplotlib.pyplot as plt

random.choice([1,2,3,4,5,6]) #this line throws the dice one time 

rolls = []              
              
for k in range(100):#we can try 1000, 10000000 times. We can notice that the histogram gets more flat when the number of rolling times increases.
    rolls.append(random.choice([1,2,3,4,5,6]))#in this case, after using for loop, we wre rolling the dice 100 times    
        
print(len(rolls))


#draw a histogram

plt.figure()
plt.hist(rolls, bins = np.linspace(0.5,6.5,7));
plt.show()


#This time we will roll 10 dice not jsut one
ys = []
for rep in range(100):#By increasing the number of dice rolls for each dice the distrbution follows the central limit theorem
#The central limit theorem (CLT) states that the sum of a large number of random variables regardless of their distribution will
#approximately follow a normal distribution (or Gaussian distribution).
    y = 0
    for k in range (10):
        x = random.choice([1,2,3,4,5,6])
        y = y + x
    ys.append(y)
    
print(len(ys)) #100

print(min(ys)) 

print(max(ys)) 

plt.figure()
plt.hist(ys); #the semicolon suppresses the output 
plt.show()





