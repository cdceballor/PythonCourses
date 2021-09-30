arr = [10,11,13,14]

def workingArr1(arr):
    print(arr)
    arr.append(15)
    print(arr)
    print(arr[-2])

def countArr(arr):
    numValue = len(arr)
    print(numValue)
    
def deletingArrV(arr):
    del arr[0]
    print(arr)
    arr.remove(11)
    print(arr)
    newArr = arr.pop(0)
    print(newArr)

def modArr(arr):
    arr[1] = "new Value"
    print(arr)

def concatArr(arr):
    con = [15,16,17,18]
    newArr = arr+con
    print(newArr)
    
def repeatArr(arr):
    neArr= arr*5
    print(neArr)
    
repeatArr(arr)