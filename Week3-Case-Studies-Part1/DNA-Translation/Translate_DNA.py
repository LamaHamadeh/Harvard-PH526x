#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:55:21 2017

@author: lamahamadeh
"""
'''
Case Study about DNA translation
'''

'''
NCBI is the United States' main public repository of DNA and related information
We will download two files from NCBI: the first is a strand of DNA and the second 
is the protein sequence of amino acids translated from this DNA.
'''

#Downloading DNA Data
#---------------------

#read in the NCBI DNA sequence with the accession number NM_207618.2
#we have downloaded two files from the website:
#DNA.txt
#protein.text

#Importing DNA Data Into Python
#-------------------------------
print("The DNA Sequence From the NCBI Website (Accession Number NM_207618.2) Is....\n")
inputfile = "DNA.txt"
f = open (inputfile, "r") #"r" here refers to reading command
seq = f.read()
seq = seq.replace("\n", "") 
seq = seq.replace("\n", "")#As strings are immutable, this method return a new string 
#so in order for us to use a new string, we have to assign it to a variable
#in this case, we will reassign it to the same variable as before.
print(seq)

#Translating the DNA Sequence
#-----------------------------
