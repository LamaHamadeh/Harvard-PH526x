# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 11:38:28 2016

@author: Lama Hamadeh
"""

while True: #the program keeps asking me to enter a number until the input is not a number 
#this step can be excluded if we want to check a single number not a whole punch of numbers

    number = input ("Please enter a number: ")
    
    is_prime = True #introductig the boolean
    
    for factor in range(2,number): #the range function always takes UP to the number value but not the value itself
    #meaning that range (2,number) it is actually range (2,number-1)
        if number % factor == 0: #this is the definition of a prime number
            is_prime = False
            break #to stop checking and make the program runs much faster
        
    if is_prime == True:
        print(str(number) +'  ' + "is a prime number!")
    else:
        print(str(number) +'  ' +"is NOT a prime number!")
