list1 = []

def collatz(x):
    list1.append(x)
    while x != 1:
        if x == 1:
            list1.append(1)
            continue
        elif x % 2 == 0:
            return x2(x)
        else:
            return x3_1(x)
        print (list1)
#егор
def x2(x):
    x = x / 2
    return collatz(x)

def x3_1(x):
    x=int(x*3+1)
    collatz(x)
