def fib_iter(n):
    n_minus_1 = 1
    n_minus_2 = 0

    while n > 1:
        n = n - 1
        tmp = n_minus_1
        n_minus_1 = n_minus_1 + n_minus_2
        n_minus_2 = tmp

    if n == 0:
        return n_minus_2
    elif n == 1:
        return n_minus_1


n = 1

while n < 100:
    print("f(",n,")=",fib_iter(n))
    n = n + 1