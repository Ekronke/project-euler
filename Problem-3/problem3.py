def primFac(n):
    res = 0
    d = 2
    while True:
        if (d == n):
            return res
        if (n % d == 0):
            n /= d
            d = 2
            if (d > res):
                res = d
        else:
            d += 1


print(primFac(5))
