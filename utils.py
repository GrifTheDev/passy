import os
from CPU import startNoPrint, startNormal
version = "v0.1.0".strip()

def printIntroText():
    print("\033[93m" + "================================================== \n_______     _       ______    ______  ____  ____  \n|_   __ \   / \    .' ____ \ .' ____ \|_  _||_  _| \n  | |__) | / _ \   | (___ \_|| (___ \_| \ \  / /   \n  |  ___/ / ___ \   _.____`.  _.____`.   \ \/ /  \n _| |_  _/ /   \ \_| \____) || \____) |  _|  |_ \n|_____||____| |____|\______.' \______.' |______| \n==================================================" + "\033[0m")
    print("\033[31m" + "NOTE: Passy is currently in a pre-release version (" + version + "). I'm still working on fully polishing all the features, so expect bugs and missing elements. If you have knowledge of Python and want to help develop passy, check out the GitHub repository: https://github.com/GrifTheDev/passy.\n\n" + "\033[0m" + "Welcome to passy " + version + ", the ULTIMATE password guessing, computer smashing game! So, how does this work? Simple, pick a mode and either make the computer guess a password or you take a shot yourself.\nIn any case, it ain't gonna be easy, so good luck!")

def printCategoryText():
    print("\nHere are the available categories, please pick one by typing the number next to it:\n1) Computer vs Computer\n2) Computer vs Player")
    
def categoryChoiceDetection(categoryChoice):
    while categoryChoice > 2:
        os.system("cls")
        print("\033[31m" + "\n==================================\n! Invalid input, please try again.\n==================================" + "\033[0m")  
        printCategoryText()
        categoryChoice = int(input("\033[36m" + "\n? Pick a mode: " + "\033[0m"))
    
    if categoryChoice == 1:
        computerVsComputerModes()

def printComputerModes():
    print("\nGreat choice! Here are the available modes for 'Computer vs Computer':\n" + "\033[36m" + "1)" + "\033[0m" + " Normal - The computer tries to guess a password of a length you specify. Output parameters are priority-only.\n" + "\033[36m" + "2)" + "\033[0m" + " No Print - The computer tries to guess a password of a length you specify. Output parameters are set to none, which allows for faster guessing time.\n")

def computerVsComputerModes():
    os.system("cls")
    printComputerModes()
    modeChoice = int(input("\033[36m" + "\n? Pick a mode: " + "\033[0m"))
    modeChoiceDetection(modeChoice)

def modeChoiceDetection(modeChoice):
    while modeChoice > 2:
        os.system("cls")
        print("\033[31m" + "\n==================================\n! Invalid input, please try again.\n==================================" + "\033[0m")  
        printComputerModes()
        modeChoice = int(input("\033[36m" + "\n? Pick a mode: " + "\033[0m"))
    
    if modeChoice == 1:
        startNormal()
    elif modeChoice == 2:
        startNoPrint()