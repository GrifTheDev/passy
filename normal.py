import os
from randomStringGen import *
import time

def startNormal():
    os.system("cls")
    print("So, before we can start completly torturing this poor computer, there is one more thing to do. Please specify the length of the password that needs to be guessed by the computer.")
    passwordLength = int(input("\033[36m" + "\n? Password Length: " + "\033[0m"))
    startGame(passwordLength)

def startGame(passwordLength):
    os.system("cls")
    print("\033[93m" + "! Initilazing..." + "\033[0m")

    toGuess = generateRandomString(passwordLength)
    currentGuess = ""
    passCounter = 1
    startTime = time.time()
    endTime = time.time()

    while toGuess != currentGuess:
        currentGuess = generateRandomString(passwordLength)
        endTime = time.time()
        timeCount = endTime - startTime
        
        print("| Attempt:", str(passCounter), "| Guess: ", currentGuess, "| Generated Password:", toGuess, "| Time:", str(timeCount), "sec |")

        passCounter += 1

    print("\033[36m" + "| Attempt:", str(passCounter), "| Guess: ", currentGuess, "| Generated Password:", toGuess, "| Time:", str(timeCount), "sec |" + "\033[0m")

    input("\n Press any key to exit...")