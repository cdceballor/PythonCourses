import Man
import random

man = Man.Man

def game(word):
    intents = 0
    wordToHide = changeWordToLine(word)
    while intents <= 9:
        print(wordToHide)
        option = input("Ingrese la letra: ")
        if option in word:
            changeLetter(option, wordToHide, word)
            print("ENCONTRASTE LA LETRA: " + option)
            if "-" in wordToHide:
                continue
            else:
                print("GANASTE!")
                break
        else:
            intents = intents + 1
            print(intents)
            if intents == 1:
                man.drawHead()
            elif intents == 2:
                man.drawBody()
            elif intents == 3:
                man.drawHandLeft()
            elif intents == 4:
                man.drawHandRight()
            elif intents == 5:
                man.drawFootLeft()
            elif intents == 6:
                man.drawFootRight()
            elif intents == 7:
                man.drawRope()
            elif intents == 8:
                man.drawBase()
                print ("PERDISTE")
                break
            
def changeWordToLine(word):
    numOfLetters = len(word)
    nw = list()
    for i in range(numOfLetters):
        nw.append("-")
    return nw

def compareWord(word):
    nw = changeWordToLine(word)
    print (nw, word)

def changeLineToWord(word, nw):
    wordWithoutLine = ""
    for i in range(len(nw)):
        wordWithoutLine = word[i]
    print (wordWithoutLine)
    
def changeLetter(option, nw, word):
    for i in range(len(nw)):
        if option == word[i]:
            nw[i] = option

def usingGame():
    dic = {0: "pepito", 1: "unicornio", 2: "acetaminofen", 3: "buzo", 4: "perro", 5: "esternocleidomastoideo"}
    n = random.randint(0,5)    
    game(dic[n])

usingGame()