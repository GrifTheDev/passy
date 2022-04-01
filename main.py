# Great terminal color code explanation article: https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences#4842446. 

import os
from utils import *

os.system("cls")
printIntroText()
printCategoryText()

categoryChoice = int(input("\033[36m" + "\n? Pick a mode: " + "\033[0m"))
categoryChoiceDetection(categoryChoice)






