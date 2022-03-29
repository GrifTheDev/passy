import random

def generateRandomString(length):
    usableCharacterSet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = ""
    for i in range (length):
        charToTake = random.randint(0, int(len(usableCharacterSet)) - 1)
        string += usableCharacterSet[charToTake]
    return string
