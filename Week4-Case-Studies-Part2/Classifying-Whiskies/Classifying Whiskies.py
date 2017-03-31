# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:06:40 2017

@author: ADB3HAMADL
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:17:25 2017

@author: ADB3HAMADL
"""

#In this case study we will classify scotch whiskies based on their flavor 
#characterisctics.
#------------------------------------------------------------------------------

#getting started with pandas
#---------------------------

##import pandas library which is a Python library designed to query and 
#manipulate annotated data tables

import pandas as pd 

#Two main objects in Pandas to work with: Series and DataFrame.

#Series
#-------

x = pd.Series([6,3,8,6], index = ['q', 'w', 'e', 'r']) #in case we didn't 
#specify the index, pandas will specify indicies numbers from 0 to len(x)
print (x)
print (x[['w','r']]) #if we want to look at the values that correspond to certain indicies


#there are many ways to construct a Series object in Pandas. 
#Creatign a dictionary is one of them
age = {'Tim':29, 'Jim':31, 'Pam':27, 'Sam':35}
x = pd.Series(age)
print (x)


#DataFrame
#---------

#create a dictionary
data = {'name': ['Tim', 'Jim', 'Pam', 'Sam'], 'age': [29, 31, 27, 35], 'ZIP':['02115', '02130', '67700', '00100']}
#create a DataFrame
x = pd.DataFrame(data, columns = ['name', 'age', 'ZIP'])
#show DataFrame
print (x)
#show data in specific column
print (x['name'])
#another way to show data in specific column is to use data attribute notation
print (x.name)


#Indexing
#--------

#we often need to reindex a series of a DataFrame object
#this doesn't affect the association between the index and the corresponding 
#data, but instead it essentially reorders the data in the object.
 
#reindex: Reorders the indices of a pandas Series object according to its argument

x = pd.Series([6,3,8,6], index = ['q', 'w', 'e', 'r'])
#look at the index
print (x.index)

#we can take the index, and we can construct a new Python list, which consists 
#of the same elements, the same letters, but now they have been ordered alphabetically.
print (sorted(x.index))
#or
print (x.reindex(sorted(x.index)))


#arithmetic operations
#----------------------

#Series and Data Frame objects support arithmetic operations like addition.
#If we, for example, add two Series objects together,
#the data alignment happens by index.
#What that means is that entries in the series that have the same index
#are added together in the same way we might add elements of a NumPy array.
#If the indices do not match, however, Pandas
#introduces a NAN, or not a number object, the resulting series.

x = pd.Series([6,3,8,6], index = ['q', 'w', 'e', 'r'])
y = pd.Series([7,3,5,2], index = ['e', 'q', 'r', 't']) #with different indices

print (x)
print (y)

#let's add them together
print (x+y)
#It can be seen that the last two elements have NAN values and that is due to 
#the addition between two different indices. In order to have meaningful 
#resulting values, the indicies must be the same!

#------------------------------------------------------------------------------

#Loading and inspecting data
#----------------------------
#pandas is already imported
import numpy as np

whisky = pd.read_csv('/Users/lamahamadeh/Downloads/whiskies.txt') # read the dataframe
whisky['Region'] = pd.read_csv('/Users/lamahamadeh/Downloads/regions.txt') #add 'regions.txt' as an extra column to the 'whiskies.txt' dataframe

print (whisky.head(4)) #check the first 4 samples
print (whisky.tail(4)) #check the last 4 samples

# we use iloc to index a dataframe by location
print (whisky.iloc[0:10]) #for rows
print (whisky.iloc[5:10, 0:5]) # for rows and columns

#diaplay the names of the dataframe columns
print (whisky.columns)

#creating a subset 'flavors' from the original dataframe 'whisky'
flavors = whisky.iloc[:, 2:14]
print (flavors)

#------------------------------------------------------------------------------

#Exploring Correlations
#----------------------

#check the correlation between flavours
corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors) #print hte correlation matrix

#plot the correlation matrix
import matplotlib.pyplot as plt

#plot the correlation betweeb flavors
plt.figure(figsize = (10,10))
plt.pcolor(corr_flavors) #plot the correlation matrix
plt.colorbar()

#plot the correlation betweeb whiskies among flavors
corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis('tight') #this function is to remove any white space in the plot that 
#indicates a no-data region
plt.colorbar()
# the white side on the top and on the right indicates that there is no data there.

#------------------------------------------------------------------------------

#Clustering Whiskies By Flavor Profile
#--------------------------------------

#The specific method we'll be using is called spectral co-clustering.

#Since that whiskeys in the dataset come from six different regions,
#we're going to ask the clustering algorithm to find six blocks.


#import the clustering method
from sklearn.cluster.bicluster import SpectralCoclustering

#call the clustering method
model = SpectralCoclustering(n_clusters = 6, random_state = 0)

#fit the model
model.fit(corr_whisky)

#Let's now look at the clusters that we have just uncovered
print(model.rows_) 

#If we sum all of the columns of this array,
#we can find out how many observations belong to each cluster.
print (np.sum(model.rows_,axis = 1))

#If we sum all of the rows of this array,
#we can find out how many clusters belong to each observation.
print (np.sum(model.rows_,axis = 0))

#------------------------------------------------------------------------------

#Comparing Correlation Matrices
#------------------------------





#------------------------------------------------------------------------------
