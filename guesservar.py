# -*- coding: utf-8 -*-
#Name: Xander Thompson
#Date: Nov 16, 2020
#File Name: guesservar.py

'''
Used in conjunction with pyguesser and cannot be
used without it or it will fail
'''
import random,sys

#Function that simply asks for int numbers to guess
#Returns the said amount to start the game
def start():
    amount = int(input('How many numbers would you like to guess? '))
    return amount

#Function that requires number to start, and how many
#must be guessed
#Returns a list with randomized values to be guessed
def randomlist(start=1,end=2):
    randomlist = []
    for i in range(start,end):
        randomlist.append(random.randint(0,10))
    return randomlist

#Funcion that writes the result to a file along wiht some information
def writertime(somelist, incguess):
    
    #Creates a file called pyGuesserResults
    with open ('pyGuesserResults.txt', 'w') as newfile:
        
        #Writes if the person guessing was successful or failed to guess all
        #numbers correctly under 3 guesses
        if (incguess == 3):
            newfile.write('You were unable to guess the numbers \n')
            newfile.write('Better luck next time! \n')
        else:
            newfile.write('You guessed all the numbers correctly!! Excellent job! \n')
        
        #Also writes to the file as to what the numbers actually were
        newfile.write('Numbers that shouldve been guessed from left to right: ')
        newfile.write(str(somelist))
        
#Function that requires guessed numbers, amount, and incorrect guesses
#Checks if the guessed number is equal to amount, if it is it means the person guessed them all
#Else, if incorrect guesses is 3, then it means the person didnt guess them all          
def results(guess, amount, inc):
    if (guess == amount):
        print('It seems youve guessed them all! Good job')
    elif (inc == 3):
        print('Oh no, looks like you didnt guess the number in 3 trys')
        print('Try again!')

#Function that ask if they user wants to retry
#If n then the program quits
#Else if y (or anything else) the program goes again
def retry():
    yesno = input(str('Would you like to go again? [y or n]'))
    if (yesno == 'n'):
        sys.exit()
    else:
        amount = int(input('How many numbers would you like to guess? ')) 
        incguess = 0
        numguess = 0 
        return amount, incguess, numguess