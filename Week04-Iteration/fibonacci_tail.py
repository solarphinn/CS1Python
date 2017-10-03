def fibonacci(n, nm1, nm2):
    if n == 0:
        return nm2
    elif n == 1:
        return nm1
    else:
        tmp = nm1
        nm1 = nm1 + nm2
        nm2 = tmp
        n = n - 1
        return fibonacci(n, nm1, nm2)


n = 1
count = 1
while n < 10000:
    print("ft(", n, ")=", fibonacci(n, 1, 0))
    n = n + 1