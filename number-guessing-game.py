# Implement the following game in python:

# 1. Randomly select a number between 1 and 20 | 50 | 100

#     import random                   <-- needs to go at the top of your python file

#     print random.randint(1,101)     <-- prints random number between 1 and 100

# 2. Ask the user to make a guess
#     Look at the input() function - e.g:
#         guess = input("Make a guess: ")

# 3. If correct report total number of guesses

# 4. Otherwise, report higher or lower than target number.

# Testing?
#     What kind of tests, if any, do you feel would be necessary/appropriate 
#     for your code?

import random

guessCount = 0
guessIsCorrect = False

def getMaxNum():
    num = input("Enter maximum number to guess i.e. 20(guessing number will be between 1 to 20): ")
    try:
        num = int(num)
    except:
        # Keep asking user a number if the input is not parsible to int
        num = getMaxNum()
    return num

maxNum = getMaxNum()

targetNum = random.randint(1,maxNum)

# 2. Ask the user to make a guess
#     Look at the input() function - e.g:
#         guess = input("Make a guess: ")
def getGuessNum():
    num = input("Make a guess between 1 to " + str(maxNum) + " : ")
    try:
        num = int(num)
    except:
        # Keep asking user a number if the input is not parsible to int
        num = getGuessNum()
    return num


while not guessIsCorrect:
    userGuess = getGuessNum()
    if userGuess == targetNum:
        guessCount += 1
        print("====================================")
        print("Conguraturations!")
        print("Your number of guess(es): " + str(guessCount))
        print("====================================")
        guessIsCorrect = True

    elif userGuess > targetNum:
        guessCount += 1
        print("====================================")
        print("The target number is smaller than " + str(userGuess) + ".")
        guessIsCorrect = False

    elif userGuess < targetNum:
        guessCount += 1
        print("====================================")
        print("The target number is larger than " + str(userGuess) + ".")
        guessIsCorrect = False

