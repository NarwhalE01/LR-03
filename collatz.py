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
