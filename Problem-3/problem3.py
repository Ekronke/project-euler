def primFac(n):
    res = 0
    k = n
    d = 2
    while k > 1:
        if (k % d == 0):
            if (d > res):
                res = d
            k /= d
            d = 2
        else:
            d += 1
    return res


print("Result: ", primFac(600851475143))
