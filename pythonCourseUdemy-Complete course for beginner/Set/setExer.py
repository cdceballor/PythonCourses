#cannot have mutable items
def creatingSet():
    set1 = {11,12,13,14,15,16}
    print(set1)
    #set1 = {11,12,13,14,{15,16}}
    #print(set1)
    
def opSet():
    set1 = {11,12,13,14,15,16}
    set1.add(17)
    print(set1)
    set2 = {10}
    set1.update(set2)
    print("Im here",set1)
    set1.remove(12)
    print(set1)
    set1.discard(10)
    print(set1)

def union():
    set1 = {1,2,3,4,5}
    set2 = {6,7,8,9,10}
    print(set1|set2)

def inter():
    set1 = {1,2,3,4,5,6}
    set2 = {6,7,8,9,10}
    print(set1.intersection(set2))
    print(set1 & set2)

creatingSet()
opSet()
union()
inter()