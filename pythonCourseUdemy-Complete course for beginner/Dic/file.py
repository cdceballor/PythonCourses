#Is the same thing that a json
def defDic():
    myDic = {1:"Hello", 2:"World", 4:{1,2,3,4,5}}
    print(myDic[1])
    print(myDic.get(2)) 
    myDic[3] = "!"
    print(myDic)
    print(myDic[4])
    #Is a key-value type, we play with the key and the structure give os a value
defDic()   