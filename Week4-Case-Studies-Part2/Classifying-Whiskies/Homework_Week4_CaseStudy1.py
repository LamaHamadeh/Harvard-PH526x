#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 19:04:02 2017

@author: lamahamadeh
"""

'''
===================================================
Case Study 1 - Scotch Wishkies Analysis Using Bokeh
===================================================
'''

#In this case study, we have prepared step-by-step instructions for you on how 
#to prepare plots in Bokeh, a library designed for simple interactive plotting. 
#We will demonstrate Bokeh by continuing the analysis of Scotch whiskies.

#----------------------------------------------------------------------------------------------------------------

# Exercise 1
#-----------

#Here we provide a basic demonstration of an interactive grid plot using Bokeh. 
#Execute the following code and follow along with the comments. We will later 
#adapt this code to plot the correlations among distillery flavor profiles as 
#well as plot a geographical map of distilleries colored by region and flavor 
#profile.

#Make sure to study this code now, as we will edit similar code in the 
#exercises that follow.

#Once you have plotted the code, hover, click, and drag your cursor on the plot 
#to interact with it. Additionally, explore the icons in the top-right corner 
#of the plot for more interactive options!

# First, we import a tool to allow text to pop up on a plot when the cursor
# hovers over it.  Also, we import a data structure used to store arguments
# of what to plot in Bokeh.  Finally, we will use numpy for this section as well!

from bokeh.models import HoverTool, ColumnDataSource
import numpy as np

# Let's plot a simple 5x5 grid of squares, alternating in color as red and blue.

plot_values = [1,2,3,4,5]
plot_colors = ["red", "blue"]

# How do we tell Bokeh to plot each point in a grid?  Let's use a function that
# finds each combination of values from 1-5.
from itertools import product

grid = list(product(plot_values, plot_values))
print(grid)


#------------------------------------------------------------------------------

# Exercise 2
#-----------





#------------------------------------------------------------------------------

# Exercise 3
#-----------





#------------------------------------------------------------------------------

# Exercise 4
#-----------




#------------------------------------------------------------------------------