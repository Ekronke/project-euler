# would be really nice to do in Haskell.
def squares(i):
    return i ** 2


listRang = list(range(1, 101))
listSum = sum(listRang) ** 2
listSqr = sum(list(map(squares, listRang)))
res = listSum - listSqr
print(res)
