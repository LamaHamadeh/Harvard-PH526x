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

plt.figure()
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

plt.figure()
nx.draw(er_graph(10, 0.08), node_size = 40, node_color = 'gray')

'''
if we put p = 0, then ER graph will give us N components
however, if we have p =1 then ER graph will give us only one componnet.
'''
#------------------------------------------------------------------------------

#Plotting the Degree Distribution
#---------------------------------

def plot_degree_distribution(G):
    plt.hist(list(G.degree().values()), histtype= 'step')
    plt.xlabel('Degree $k$')
    plt.ylabel('$P(k)$')
    plt.title('Degree Distribution')

plt.figure()
G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)

G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)

G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)

# we can see that the three degree distributions follow one another
#fairly closely.
#------------------------------------------------------------------------------

#Descriptive Statistics of Empirical Social Networks
#---------------------------------------------------

#The structure of connections in a network
#can be captured in what is known as the Adjacency matrix of the network.
#If we have n nodes, this is n by n matrix,
#where entry ij is one if node i and node j have a tie between them.
#Otherwise, that entry is equal to zero.
#The graphs we're dealing with are called undirected,
#which means that a tie between nodes i and j
#can just as well be described as a tie between nodes j and i.
#Consequently, the adjacency matrix is symmetric.
#That means that the element ij is always the same as the element ji.
#Either both are zero or both are equal to 1.

#import numpy
import numpy as np

#import datasets
A1 = np.loadtxt('C:/Users/Admin/Desktop/adj_allVillageRelationships_vilno_1.csv', delimiter = ',')
A2 = np.loadtxt('C:/Users/Admin/Desktop/adj_allVillageRelationships_vilno_2.csv', delimiter = ',')

#Our next step will be to convert the adjacency matrices to graph objects.
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print('Number of nodes: %d' % G.number_of_nodes())
    print('Number of edges: %d' % G.number_of_edges())
    print('Average Degree: %.2f' % np.mean(list(G.degree().values())))

basic_net_stats(G1)
basic_net_stats(G2)

plt.figure()
plot_degree_distribution(G1)
plot_degree_distribution(G2)

#Notice how the degree distributions look quite different from what
#we observed for the ER networks.
#It seems that most people have relatively few connections,
#whereas a small fraction of people have a large number of connections.
#This distribution doesn't look at all symmetric,
#and its tail extends quite far to the right.
#This suggests that the ER graphs are likely not good models
#for real world social networks.
#In practice, we can use ER graphs as a kind of reference graph
#by comparing their properties to those of empirical social networks.
#More sophisticated network models are able to capture
#many of the properties that are shown by real world networks.

#------------------------------------------------------------------------------

#Finding the Largest Connected Component
#---------------------------------------

G1_LCC = max(nx.connected_component_subgraphs(G1), key=len)
G2_LCC = max(nx.connected_component_subgraphs(G2), key=len)

print(G1_LCC) #this would give us the same output as if we print 
#G1_LCC.number_of_nodes()

print G1_LCC.number_of_nodes() / G1.number_of_nodes()
#in this case, we see that 97.9% of all of the nodes of graph G1
#are contained in the largest connected component.

print G2_LCC.number_of_nodes() / G2.number_of_nodes()
#for G2 have approximately 92% of all nodes
#are contained in the largest connected component.

#Let's now try visualizing these components.
#for G1
plt.figure()
nx.draw(G1_LCC, node_color = 'red', edge_color = 'gray', node_size = 20)

#for G2
plt.figure()
nx.draw(G2_LCC, node_color = 'green', edge_color = 'gray', node_size = 20)

#The visualization algorithm that we have used
#is stochastic, meaning that if you run it several times,
#you will always get a somewhat different graph layout.
#However, in most visualizations, you should
#find that the largest connected component of G2
#appears to consist of two separate groups.
#These groups are called network communities.
#And the idea is that a community is a group
#of nodes that are densely connected to other nodes in the group,
#but only sparsely connected nodes outside of that group.

#------------------------------------------------------------------------------
