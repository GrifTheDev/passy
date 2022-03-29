# Great terminal color code explanation article: https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences#4842446. 

import os

def printIntroText():
    print("\033[93m" + "================================================== \n_______     _       ______    ______  ____  ____  \n|_   __ \   / \    .' ____ \ .' ____ \|_  _||_  _| \n  | |__) | / _ \   | (___ \_|| (___ \_| \ \  / /   \n  |  ___/ / ___ \   _.____`.  _.____`.   \ \/ /  \n _| |_  _/ /   \ \_| \____) || \____) |  _|  |_ \n|_____||____| |____|\______.' \______.' |______| \n==================================================" + "\033[0m")
    print("Welcome to passy, the ULTIMATE password guessing, computer smashing game! So, how does this work? Simple, pick a mode and either make the computer guess a password or you take a shot yourself.\nIn any case, it ain't gonna be easy, so good luck!")

def printCategoryText():
    print("\nHere are the available categories, please pick one by typing the number next to it:\n1) Computer vs Computer\n2) Computer vs Player")

def computerVsComputerModes():
    print("Great choice! Here are the available modes for 'Computer vs Computer':\n")

os.system("cls")
printIntroText()
printCategoryText()

categoryChoice = int(input("\033[36m" + "\n? Pick a mode: " + "\033[0m"))

while categoryChoice > 2:
    os.system("cls")
    print("\033[31m" + "\n==================================\n! Invalid input, please try again.\n==================================" + "\033[0m")  
    printCategoryText()
    categoryChoice = int(input("\033[36m" + "\n? Pick a mode: " + "\033[0m"))

if categoryChoice == 1:
    computerVsComputerModes()
