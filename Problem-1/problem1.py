def summation(a, i, iMax, r):
    if (i > iMax):
        return r
    r = r + a*i
    i += 1
    return summation(a, i, iMax, r)


sum3 = summation(3, 1, 333, 0)
sum5 = summation(5, 1, 199, 0)
sum15 = summation(15, 1, 66, 0)
result = sum3 + sum5 - sum15

print(result)
