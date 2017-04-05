# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 10:31:34 2017

@author: Admin
"""


#Introduction to GPS Tracking of Birds
#-------------------------------------

#load the dataframe
import pandas as pd 

birddata = pd.read_csv('bird_tracking.csv')

print(birddata.head(5))
print(birddata.shape)#61920x8
print(birddata.columns)

#------------------------------------------------------------------------------

#Simple Data Visualizations
#---------------------------

import matplotlib.pyplot as plt
import numpy as np

#plot latitude and longitude on a simple 2D plot for one bird (e.g., Eric)
ix = birddata.bird_name == 'Eric'
x , y = birddata.longitude[ix] , birddata.latitude[ix]
plt.figure(figsize=(7,7))
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.plot(x,y) #the plot shows the path that Eric has taken.


##plot latitude and longitude on a simple 2D plot for all the three birds
bird_names = pd.unique(birddata.bird_name)

plt.figure(figsize=(7,7))

for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x , y = birddata.longitude[ix] , birddata.latitude[ix]
    plt.plot(x,y,'.',label = bird_name)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(loc='lower right')
   
# Looking at the plot, we see that all three birds
#seem to have pretty similar overall flight patterns.
#However, Nico and Sanne seem to venture out further south than Eric does.

#------------------------------------------------------------------------------

#Examining Flight Speed
#-----------------------

#examining the flight speed for 'Eric'
ix = birddata.bird_name == 'Eric'
speed = birddata.speed_2d[ix]

#if we want to know hpw many nans are there for Eric in particular
np.sum(np.isnan(speed)) #85
ind = np.isnan(speed)







'''
#if we want to know how many nans are there for each features in the datatset
#identify NANs
#--------------
def num_missing(x):
  return sum(x.isnull())

#Applying per column:
print ("Missing values per column:")
print (birddata.apply(num_missing, axis=0)) #axis=0 defines that function is to be applied on each column

# it can be seen that both 'direction' and 'speed_2d' have 443 nans each.
'''



#------------------------------------------------------------------------------

#Using Datetime
#--------------




#------------------------------------------------------------------------------

#Calculating Daily Mean Speed
#-----------------------------





#------------------------------------------------------------------------------

#Using the Cartopy Library
#-------------------------



#------------------------------------------------------------------------------
