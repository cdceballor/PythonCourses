
word = {
    "phone": "A device to play video games and make calls",
    "house": "Where the people live"
    }

def addWord(word,w, description):
    print(word)
    word[w] = description
    print(word)

def lookExist(word, w):
    if w.lower() in  word:
        print(word[w])
    else:
        description = input("Ingrese su descripción: ")
        addWord(word, w, description)

def executor():
    w = input("Ingrese la palabra que quiere almacenar: ")
    lookExist(word, w)

executor()                
                