

def factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    elif n == 1:
        return accumulator
    else:
        accumulator = accumulator * n
        n = n - 1
        return factorial(n, accumulator)


print(factorial(100))