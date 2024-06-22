# Read wrong
def primfind(n):
    d = 2
    num = n
    i = 1
    primCount = 1
    while primCount < 10001:
        if (num % d == 0):
            if (num == d):
                primCount += 1
            else:
                num = n + i
                i += 1
                d = 2
        else:
            d += 1


print(primfind(10001))
