import random
import os
import time

print("! Initilazing...")

def generateRandomPass(length):
    usableCharacterSet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passowrd = ""
    for i in range (size):
        charToTake = random.randint(0, int(len(usableCharacterSet)) - 1)
        passowrd += usableCharacterSet[charToTake]
    return passowrd

def generateGuess(length):
    usableCharacterSet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    guess = ""
    for i in range (size):
        charToTake = random.randint(0, int(len(usableCharacterSet)) - 1)
        guess += usableCharacterSet[charToTake]
    return guess

def printStart():
    os.system("cls")
    print("=========================PASSY [V0.1.0]=========================")
    print("Welcome to passy, the ULTIMATE battle between a computer and a computer! That's right, the computer fights itself, but how?\n\nPassy is a password guessing game where the computer will generate a random passowrd, the size of which will be your choice, and then it tries to guess it. How fun!\n\nTo begin, input the password size below!")
    print("================================================================")

def guess():
    toGuess = generateRandomPass(size)
    currentGuess = ""
    passCounter = 1
    startTime = time.time()
    endTime = time.time()
    while toGuess != currentGuess:
        currentGuess = generateGuess(size)
        endTime = time.time()
        timeCount = endTime - startTime
        
        print("| Attempt:", str(passCounter), "| Guess: ", currentGuess, "| Generated Password:", toGuess, "| Time:", str(timeCount), "sec |")

        passCounter += 1

    print("| Attempt:", str(passCounter), "| Guess: ", currentGuess, "| Generated Password:", toGuess, "| Time:", str(timeCount), "sec |")

printStart()
size = int(input("? Password Size: "))
guess()







