print(True and True)
print(True and False)

def braking():
    for i in range(1,11):
        if i == 5:
            #Stop in 5
            break
    print(i)

def continuing():
    for i in range(1,11):
        if i == 5:
            #Jump the 5 value
            continue
    print(i)

def exception():
    try:
        x = 9
        raise ZeroDivisionError
    except ZeroDivisionError:
        print("Division 0")
    finally:
        print("nothing")

def ciclo():
    for i in range(1,11,1): #start, final value, iteration
        print(i)