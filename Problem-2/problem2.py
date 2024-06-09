def fib(n):
    r = 2
    f0 = 1
    f1 = 2
    i = 1
    while True:
        fn = f0 + f1
        print(fn)
        f0 = f1
        f1 = fn
        if (fn > n):
            return r
        if (i % 3) == 0:
            r += fn
        i += 1


print("Result", fib(4000000))
