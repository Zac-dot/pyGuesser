#Name: Xander Thompson
#Date: Nov 16, 2020
#File Name: pyguesser.py

import guesservar as vars


#Asking for the amount of numbers to guess
amount = vars.start()

#Calling defined function to randomize
lista = vars.randomlist(0,amount)

#variable to keep tally as to what number is guessed
numguess = 0

#variable to tally incorrect guesses
#when it hits three the game is over
incguess = 0

#simple message letting them know its successful, also saying to guess the firs digit
print('The numbers...have been randomized!!')
print('Lets guess what number', numguess+1, 'is!')

#Checking up to see if all numbs have been guessed
while True:

    #Grabs the guessed number between 1 and 10
    guessednum = int(input('Please guess a number between 0-10: \n'))
    
    #Checking the number to see if its correct
    if (guessednum == lista[numguess]):
        
        #Prints saying that the number was correct if it was
        print('Hey!', guessednum, 'was the right number!')
        
        #Adds to numguess to increase amount
        numguess = numguess + 1
        
        #Breaks the loop if all numbers are guessed
        if (numguess == amount):
            #Calls a function to let person know if they guessed them correctly
            vars.results(guessednum, amount, incguess)
            
            #Calls a function to write the results to a file
            vars.writertime(lista,incguess)
        
            #Asks if they want to retry
            vars.retry()
            
        #Resets the incorrect guesses back to 0
        incguess = 0
        
        #Onto next number if possible
        print('On to the next number!')
        
    #Statements for if the entered number is too big or small          
    elif (guessednum > lista[numguess]):
        print('Hmm, that number was too big. Guess again!')
        incguess = incguess + 1
    elif (guessednum < lista[numguess]):
        print('Hmm, that number was a tad small. Guess again!')
        incguess = incguess + 1
    else:
        print('Did you guess between 0 and 10? Please check and guess again')
    
    #Ends the game if incorrect guesses = 3
    if (incguess == 3):
        #Calls a function to let person know if they guessed them correctly
        vars.results(guessednum, amount, incguess)
    
        #Calls a function to write the results to a file
        vars.writertime(lista,incguess)
        
        #Asks if they want to retry
        vars.retry()

    
    
    
