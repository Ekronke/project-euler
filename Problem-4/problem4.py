# Stupid brute force method

def palindrom(i):
    numStr = str(i)
    revNum = numStr[::-1]
    result = False
    if (numStr == revNum):
        result = True
    return result


def multMaker(a, b):
    print(a, b)
    c = 0
    currC = 0
    res = (0, 0)
    while (a > 900 and b > 900):
        print(c)
        c = a * b
        if (palindrom(c) and currC < c):
            currC = c
            res = (a, b, currC)
        a -= 1
        if (a < 992):
            b -= 1
            a = 999
    return res


print(multMaker(999, 999))
