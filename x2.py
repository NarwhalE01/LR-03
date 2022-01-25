def x2(x):
    x = x / 2
    list1.append(x)
    return collatz(x)

def x3_1(x):
    x = x*3+1
    list1.append(x)
    return collatz(x)
