#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:55:21 2017
@author: Lama Hamadeh
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
#we can/need enter the studying folder through 'cd' and display the current folder using 'pwd'

print("\nThe DNA Sequence From the NCBI Website (Accession Number NM_207618.2) Is....\n")
inputfile = "DNA.txt"
f = open (inputfile, "r") #"r" here refers to reading command
seq = f.read()
seq = seq.replace("\n", "") 
seq = seq.replace("\n", "")#As strings are immutable, this method return a new string 
#so in order for us to use a new string, we have to assign it to a variable
#in this case, we will reassign it to the same variable as before.
print(seq) #we can even slice up the sequence to see specific part of the DNA file
#for example: print(seq[40:50]). In this case the output would be: CCTGAAAACC.

#Translating the DNA Sequence
#-----------------------------
#the translation process is essentially a table lookup operation.
#Python provides a very natural object for dealing with these types of situations.
#The object is a dictionary.
#In this case, the key objects are strings, each consisting of three letters, 
#i.e., condons or nucleotide triples, drawn 
#from the four letter alphabet (A,G,C,T).
#The value object is also a string but a string consisting of just one-letter symbol
#used for different amino acids.

#Defining a dictionary called 'table':
table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
         'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
         'AAC':'N', 'AAt':'N', 'AAA':'K', 'AAG':'K',
         'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
         'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
         'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
         'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
         'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
         'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
         'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
         'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
         'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
         'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
         'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
         'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
         'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


print (table['ATC']) #to see what is the corresponding value for the key ATC.

#STEP1: Check that length of sequence is divisible by 3

#STEP2: Look up each 3-letter string in table and store result.

#STEP3: Continue lookups until reaching end of sequence.

#Define a function that describes the translating process.

def translate(seq):
    '''DOCSTRING: Translate a string containing a nucleotide sequence into a string containing the corresponding 
    sequence of amino acids. Nucleotides are translated in triplets using the table dictionary; each 
    amino acid is encoded with a string of length 1.'''
    
    table = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
         'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
         'AAC':'N', 'AAt':'N', 'AAA':'K', 'AAG':'K',
         'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
         'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
         'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
         'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
         'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
         'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
         'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
         'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
         'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
         'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
         'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
         'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
         'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    protein = ''
    if len(seq) % 3 == 0: # Check that length of sequence is divisible by 3
        for i in range(0, len(seq), 3): #Look up each 3-letter string in table and store result.
            condon = seq[i : i+3]
            protein += table[condon]
                
    return protein


#check the function

print(translate("ATG"))

print(help (translate))#This print the docstring that is included inside the function



