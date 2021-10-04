#We cannot change the value inside of a tuple, but in a list yes

def createTupla():
    tuple1 =()
    tuple2 =(1,2,3)
    tuple3 =(1,"2",3, 4, "5", [1,2,3, "3"])
    print(tuple1)
    print(tuple2)
    print(tuple3)
    print(tuple3[5])
    print(tuple3[5][1])
    print(tuple3[1:3]) # The last number is exclusive

createTupla()

def countingTupla():
    tuple1 = ("s","d","d","d","d","f","f","g","h","j","j","r","e","e","e","d","s","g","f","s","a","a")
    print(tuple1.count("d"))
    print(tuple1.index("s"))
    tuple2 = (1,2,3,4,5,6,7,8,9,10,11,12,13)
    print(max(tuple2))
    print(min(tuple2))
    print(sorted(tuple2))
    print(len(tuple2))
    
countingTupla()