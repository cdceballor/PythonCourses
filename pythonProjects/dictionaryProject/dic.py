
word = {
    "phone": "A device to play video games and make calls",
    "house": "Where the people live"
    }

def addWord(word,w, description):
    print(word)
    word[w] = description
    print(word)

def lookExist(word, w):
    if w in  word:
        print(word[w])
    else:
        description = input("Ingrese su descripción: ")
        addWord(word, w, description)


def writting(word):
    f = open ('holamundo.txt','w')
    f.write(str(word))
    f.close()
    
def executor():
    while True:
        w = input("Ingrese la palabra que quiere almacenar: ")
        lookExist(word, w.lower())
        writting(word)
executor()                
                