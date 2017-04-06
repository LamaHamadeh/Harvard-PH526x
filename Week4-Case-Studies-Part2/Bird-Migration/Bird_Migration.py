# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 10:31:34 2017
@author: Lama Hamadeh
"""


#Introduction to GPS Tracking of Birds
#-------------------------------------

#load the dataframe
import pandas as pd 

birddata = pd.read_csv('/Users/Admin/Desktop/bird_tracking.csv')

print(birddata.head(5))
print(birddata.shape)#61920x8
print(birddata.columns) #print columns titles

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
ind = np.isnan(speed) 
#if we want to know hpw many nans are there for Eric in particular
#np.sum(np.isnan(speed)) #85
plt.hist(speed[~ind])
#we have taken the bitwise complement of the 'ind' array which turns each occurence
#of true to a false and vice versa.


plt.figure(figsize = (8,4))
speed = birddata.speed_2d[birddata.bird_name == 'Eric']
ind = np.isnan(speed)
plt.hist(speed[~ind], bins = np.linspace(0, 30, 20), normed = True)
plt.xlabel('2D speed (m/s)')
plt.ylabel('Frequency')


#ploting histograms using pandas instead of plt
#in this case, the plotting functions are methods of dataframe instances

birddata.speed_2d.plot(kind = 'hist', range = [0,30])
plt.xlabel('2D speed')

#The benefit of using pandas in this case was that we did not
#have to deal with NaNs explicitly.
#Instead, all of that happens under the hood.


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

import datetime 

datetime.datetime.today()

time_1 = datetime.datetime.today()

print (time_1)

time_2 = datetime.datetime.today()

print (time_2)

print(time_2 - time_1) #this is the so-called timedelta

#If we'd like to compute how much time has passed between any two
#observations in our data set, we first have
#to convert the timestamps, now given as strings, to datetime objects.

date_str = birddata.date_time[0]

print(date_str)
print(date_str[:-3]) #this will slice the given time by removing the last three
#characters.

datetime.datetime.strptime(date_str[:-3], '%Y-%m-%d %H:%M:%S')
#Here datetime.datetime.strptime Takes in a date and time string, as well as 
#an expected format string, and returns a formatted datetime object.

#We can now use this function to go over every single row in our data set,
#and create a new datetime object corresponding to every single row.

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3],'%Y-%m-%d %H:%M:%S'))
    
    
birddata['timestamp'] = pd.Series(timestamps, index = birddata.index) #this will
#add the homemade created 'timestamps' list ot as an extra column to our 
#dataframe 'birddata'. 

#What I'd like to do next is to create a list that
#captures the amount of time that has elapsed
#since the beginning of data collection.

#STEP1: First I will extract the timestamps for Eric,
#and that object is going to be called times.
times = birddata.timestamp[birddata.bird_name == 'Eric']

#STEP2: then create my elapsed time object and I
#construct that as a list comprehension.
elapsed_time = [time - times[0] for time in times]

print(elapsed_time[1000])

plt.plot(np.array(elapsed_time) / datetime.timedelta(days = 1))
plt.xlabel('Observation')
plt.ylim((0,300))
plt.ylabel('Elapsed time (days)')

#------------------------------------------------------------------------------

#Calculating Daily Mean Speed
#-----------------------------
data = birddata[birddata.bird_name == 'Eric']
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days = 1)
next_day = 1
inds = []
daily_mean_speed = []
for (i,t) in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []
        
plt.figure(figsize = (8,6))
plt.plot(daily_mean_speed)
plt.xlabel('Day')
plt.ylabel('Daily Mean Speed (m/s)')


#------------------------------------------------------------------------------

#Using the Cartopy Library
#-------------------------

import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mecrator()

plt.figure(figsize = (10,10))
ax = plt.axes(projection = proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle = '.')


for name in bird_names:
    ix = birddata['bird_name'] == name
    x , y = birddata.logitude[ix], birddata.latidute[ix]
    ax.plot(x,y,'.', transform = ccrs.Geodetic(), label = name)
    
plt.legeng(loc = 'upper left')
#------------------------------------------------------------------------------
