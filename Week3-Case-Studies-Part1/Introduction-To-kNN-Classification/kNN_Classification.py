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
    
print (distance(p1,p2))

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

votes = [1, 2, 3, 1, 2 ,3 ,3 ,3 ,3, 2, 2, 2] #here number 2 and 3 has the same appearing frequency: 5 (tie situation)
winner = majority_vote(votes)
print (winner) #it can be seen after running the code several times that this method picks one of the candidates
#and returns it randomly.

#another method
#--------------
import scipy.stats as ss

def majority_vote_short(votes):
    "Return the most common element in votes "
    mode , count = ss.mstats.mode(votes)  
    return mode

votes = [1, 2, 3, 1, 2 ,3 ,3 ,3 ,3]
winner_short = majority_vote_short(votes)
print (winner_short) # it can be seen after running the code several times that this method always 
#returns number 3 as the most common candidate and forgets about the other one: 2

#------------------------------------------------------------------------------

#Finding Nearest Neighbors
#--------------------------

points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]]) #points as a vector
p = np.array([2.5,2])#a single point with coordinates: x=2.5 and y=2

#plotting the points and point p
import matplotlib.pyplot as plt

plt.plot(points[:,0], points[:,1],"ro")
plt.plot(p[0],p[1],"bo")
plt.axis([0.5, 3.5, 0.5, 3.5])

distances = np.zeros(points.shape[0])#'.shape[0]' here reutrn a tuple of array dimensions.
for i in range(len(distances)):# loop over all points
    distances[i] = distance(p,points[i]) # compute the distance between point p and every other point using the function 'distnace'
        

print(distances)#reutrn the distances values between all the points and the point p
print(points[4])#return the point number 4
print(distances[4])#calculate the distnace between point number 4 and point p
print(points[7])#return the point 7
print(distances[7])#calculate the distnace between point number 7 and point p

#construct a 'find_nearest_neighbor' function
def find_nearest_neighbor(p, points, k=5):
    """find the k nearest neighbors of point p nd return their indices """
    distances = np.zeros(points.shape[0])#'.shape[0]' here reutrn a tuple of array dimensions.
    for i in range(len(distances)):# loop over all points
        distances[i] = distance(p,points[i]) # compute the distance between point p and every other point using the function 'distnace'
    ind = np.argsort(distances)#'argsort' is a function that sorts the distnaces indinces from short to long.
    #np.argsort(distances) it sorts an array according to a single argument and returns the sorted indices
    return ind[0:k] # or for short ind[:k]. This step is to return those k points that are nearest to point p


ind = find_nearest_neighbor(p, points, 2); print(points[ind])# return the first 2 nearest neighbors
ind = find_nearest_neighbor(p, points, 3); print(points[ind])# return the first 3 nearest neighbors
ind = find_nearest_neighbor(p, points, 4); print(points[ind])# return the first 4 nearest neighbors

#construct a 'knn_predict' function
def knn_predict(p, points, outcomes, k=5):
    #find k nearest neighbors
    ind = find_nearest_neighbor(p, points, k)
    return majority_vote(outcomes[ind])
    #predict the class/ categroy of p based on majority vote

outcomes = np.array([0,0,0,0,1,1,1,1,1]) # classes definition

print(len(outcomes))

print(knn_predict(np.array([2.5, 2.7]), points, outcomes, k=2)) #class 1
print(knn_predict(np.array([1.0, 2.7]), points, outcomes, k=2)) #class 0


#------------------------------------------------------------------------------

#Generating Synthetic Data
#-------------------------

def generate_synthetic_data(n=50):
    """Create two sets of points from bivariate normal distributions."""
    points = np.concatenate((ss.norm(0,1).rvs((n,2)),ss.norm(1,1).rvs((n,2))), axis=0) #norm(mean, standard deviation)
    #'.rvs' Random variates of given type. Here we have: .rvs((number of rows, number of columns))
    # 'axis = 0' means that we are concatenating along the rows of these arrays
    outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n)))
    #0 and 1 here refer to the names of classes
    return (points, outcomes)

n=20

(points, outcomes) = generate_synthetic_data(n) #this gives 20 points from class 0 and the other 20 from class 1

plt.figure()
plt.plot(points[:n,0], points[:n,1], "ro") #this refers to the first class 0 (n points)
plt.plot(points[n:,0], points[n:,1], "bo") #this refers to the second class 1 (n points)


#------------------------------------------------------------------------------

#Making a Prediction Grid
#-------------------------

def make_prediction_grid(predictors, outcomes, limits, h, k):
    """classify each point on the prediction grid."""
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    
    prediction_grid = np.zeros(xx.shape, dtype = int) # the type here is 'int' becasue both classes are integers: either 0 or 1
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
            #It can be noticed here that we have put [j,i] not the other way around. The reason for that is
            #
    return (xx, yy, prediction_grid)

#------------------------------------------------------------------------------

#Plotting the Prediction Grid
#-----------------------------

def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)
    
    
(predictors, outcomes) = generate_synthetic_data()


k = 5; filename = "knn_synth_5.pdf"; limits = (-3, 4, -3 ,4); h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h ,k)
plot_prediction_grid(xx, yy, prediction_grid, filename)


k = 50; filename = "knn_synth_50.pdf"; limits = (-3, 4, -3 ,4); h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h ,k)
plot_prediction_grid(xx, yy, prediction_grid, filename)

#Looking at the plot for k equals 50, we can see that the decsionboundary is pretty smooth.
#In contrast, if you look at the plot where k equals to 5, you'll see that the shape of the descison boundary is more complicated. 
#It seems that you might be able to find a value of k that maximises the accuracy of the predictions.
#But that's somewhat short sighted. 
#this is because what you really care about is not how well your method performs on the training data set, 
#the data set that we have seen so far.
#but rather how well it performs on a future dataset you have not yet seen. 
#It turns out that using a value for k that is too large or too small is not optimal. 
# a phenomenon that is known as the bias-variance tradeoff. This suggests that some intermediate values of k
#might be best. 

#------------------------------------------------------------------------------

#Applying the kNN Method
#------------------------

from sklearn import datasets
iris = datasets.load_iris()

print iris.data

predictors = iris.data[:, 0:2]
outcomes = iris.target

plt.plot(predictors[outcomes==0][:,0],predictors[outcomes==0][:,1],'ro') #the first species/ feature that is contained in the iris dataset
plt.plot(predictors[outcomes==1][:,0],predictors[outcomes==1][:,1],'go') #the second species/ feature that is contained in the iris dataset
plt.plot(predictors[outcomes==2][:,0],predictors[outcomes==2][:,1],'bo') #the third species/ feature that is contained in the iris dataset

#prediction plot
k = 5; filename = "iris_grid.pdf"; limits = (4,8,1.5,4.5); h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h ,k)
plot_prediction_grid(xx, yy, prediction_grid, filename)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)


print sk_predictions.shape #(150,)


my_predictions = np.array([knn_predict(p,predictors, outcomes,5) for p in predictors])

print my_predictions.shape # (150,)


sk_predictions == my_predictions

print np.mean(sk_predictions == my_predictions) 
print 100*np.mean(sk_predictions == my_predictions) #precentage

print 100*np.mean(sk_predictions == outcomes) #83.333
print 100*np.mean(my_predictions == outcomes) #84.666

# It can be seen clearly that our homeade predictors is slightly better than the sklearn predictior: it is accurate approximately 85% of the time.

#------------------------------------------------------------------------------
