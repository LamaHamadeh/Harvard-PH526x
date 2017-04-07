#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 7 10:37:22 2017

@author: lamahamadeh
"""

#Basics of NetworkX
#-------------------

#import networkx module
#----------------------
import networkx as nx


#Creat a Graph
#-------------
G = nx.Graph()


#nodes
#-----
G.add_node(1) #add one numeric node
G.add_nodes_from([2,3]) #add a list of numeric nodes
G.add_nodes_from(['u', 'v']) #add a list of string nodes
G.nodes() #show the nodes in our graph
G.remove_node(2) #remove one node from the graph
G.remove_nodes_from([4,5]) #remove a list of nodes form graph
G.nodes() #to see the remaining nodes
G.number_of_nodes() #to see how many nodes in the graph


#Edges
#-----
G.add_edge(1,2) #add one edge. it has to be a tuple
G.add_edge('u','v') #add a string edge
G.add_edges_from([(1,3),(1,4),(1,5),(1,6)]) #a list of numeric edges
G.add_edge('u', 'w')#add a list of string edges
G.edges() #show the edges in our graph
G.remove_edge(1,3) #remove one edge from graph
G.remove_edges_from([(1,2), ('u', 'v')])#remove a list of edges
G.edges() #to see the remaining edges
G.number_of_edges() #to see how many edges in the graph

#------------------------------------------------------------------------------

#Graph Visualization
#-------------------

#We will use one of the datasets that are contained in networkx  called 
#the karate club graph.

#In this network, the nodes represent members of a karate club and the edges
#correspond to friendships between the members.


#We can extract the karate club data by typing karate club graph
G = nx.karate_club_graph()

import matplotlib.pyplot as plt

nx.draw(G, with_labels = True, node_color = 'lightblue', edge_color = 'gray')

#Networkx stores the degrees of nodes in a dictionary where
#the keys are node IDs and the values are their associated degrees.
G.degree()[33]
G.degree(33)

print (G.number_of_nodes(), G.number_of_edges())
print (G.degree(0) is G.degree()[0])

#------------------------------------------------------------------------------

#Random Graphs
#-------------

#Our task here is to create our own ER graph

from scipy.stats import bernoulli

def er_graph(N, p):#N is the number of nodes
                   #p is the probability of any pair of nodes to be connected 
                   #by an edge
    """Generate an ER graph. """
    #create an empty graph
    G = nx.Graph()
    #add all N nodes in the graph
    G.add_nodes_from(range(N)) #from 0 to N-1
    #loop over all pairs of nodes
    for node1 in G.nodes():
        for node2 in G.nodes():
            # add an edge with probability p
            if node1 < node2 and bernoulli.rvs(p=p): 
            #the first p is the the name of the keyward argument that we're providing
            #the second p is the actual value of p, in this case 0.2
            #we have add the additional constraint of node1<node2 to make the 
            #function connects between a pair of nodes only one time.
                G.add_edge(node1, node2)
    return G


print (G.number_of_nodes()) #20

nx.draw(er_graph(10, 0.08), node_size = 40, node_color = 'gray')

'''
if we put p = 0, then ER graph will give us N components
however, if we have p =1 then ER graph will give us only one componnet.
'''
#------------------------------------------------------------------------------

#Plotting the Degree Distribution
#---------------------------------





#------------------------------------------------------------------------------

#Descriptive Statistics of Empirical Social Networks
#---------------------------------------------------





#------------------------------------------------------------------------------

#Finding the Largest Connected Component
#---------------------------------------





#------------------------------------------------------------------------------