def vvod():
    while True:
        n = int(input("Введите натуральное число: "))
        if n > 0:
            break
        print("Неправильное число")
    return n

def collatz(n):
    list1 = [n]
    if n == 1:
        pass
    elif n % 2 == 0:
        list1.extend(x2(n))
    else:
        list1.extend(x3_1(n))
    return list1

def x2(n):
    return collatz(n // 2)

def x3_1(n):
    return collatz(n * 3 + 1)

if __name__ == '__main__':
    x = vvod()
    print(collatz(x))