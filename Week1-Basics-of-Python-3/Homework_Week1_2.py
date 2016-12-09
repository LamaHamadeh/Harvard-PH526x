# -*- coding: utf-8 -*-
"""
Created on Fri Dec 09 14:12:45 2016

@author: Lama Hamadeh
"""

#The ratio of the areas of a circle and the square inscribing it is pi / 4. 
#In this six-part exercise, we will find a way to approximate this value.

#-------------------------------------------------

#2a
#Using the math library, calculate and print the value of pi / 4.


import math
from math import pi

x = math.pi/4

#print(x)

#-------------------------------------------------

#2b
#Using random.uniform, create a function rand() that generates a single float between -1 and 1.
#Call rand() once. So we can check your solution, we will use random.seed to fix the value called 
#by your function.


import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
   return random.uniform(-1, 1)

rand()

#-------------------------------------------------

#2c
#The distance between two points x and y is the square root of the sum of squared differences along 
#each dimension of x and y. Create a function distance(x, y) that takes two vectors and outputs the 
#distance between them. Use your function to find the distance between (0,0) and (1,1).
#Print your answer.

def distance(x, y): #x,y are points 
    dist = math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 )#the first point x=(x0,y0)
    #and the second point y=(x1,y1). The distance between two points is given by:
        #distance = sqrt((x0-x1)^2+(y0-y1)^2)
    return dist
    
print(distance((0,0),(1,1)))

#-------------------------------------------------

#2d
#distance(x, y) is pre-loaded from part 2c. Make a function in_circle(x, origin) that uses distance 
#to determine if a two-dimensional point falls within the the unit circle with a given origin. 
#That is, find if a two-dimensional point has distance <1 from the origin (0,0).
#Use your function to print whether the point (1,1) lies within the unit circle centered at (0,0).

def in_circle(x, origin = [0]*2):
   return distance(x, origin) < 1
   
print(in_circle( (1,1) ))

#-------------------------------------------------

#2e

    


