def fibonacci(N):
    """
    Returns the value of the Nth number in the Fibonacci sequence using the
    recursive mathematical formula:
    F(1) = 1
    F(2) = 2
    F(N) = F(N-1) + F(N-2) for any N > 2
    :param N: The index of the number in the Fibonacci sequence.
    :return: The Nth number in the Fibonacci sequence.
    """
    if N == 1:
        return 1
    elif N == 2:
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)


def test_fibonacci(N):
    """
    Recursively prints all of the Fibonacci numbers from the 1st to the Nth.
    :param N: The index at which to start printing.
    :return: None
    """
    if N == 0:
        pass
    else:
        test_fibonacci(N-1)
        print(fibonacci(N))


def factorial(N):
    """
    Calculates and returns the value of N! according to the recursive formula:
    F(0) = 1
    F(1) = 1
    F(N) = N * F(N-1) for any N > 1
    :param N: The number N for which N! will be calculated.
    :return: N! (N factorial)
    """
    if N == 0:
        return 1
    elif N == 1:
        return 1
    else:
        return N * factorial(N-1)


def test_factorial(N):
    """
    Recursively prints all of the values from 0! to N!.
    :param N: The number at which to start calculating factorials.
    :return: None
    """
    if N < 0:
        return
    else:
        test_factorial(N - 1)
        print(factorial(N))


def exponent(x, y):
    """
    Calculates x^y recursively using the formula:
    F(x,0) = 1
    F(x,y) = x * F(x, y-1)
    :param x: The number to raise to a power.
    :param y: The power to which the number should be raised.
    :return: x to the y power.
    """
    if y == 0:
        return 1
    else:
        return x * exponent(x, y-1)


def test_exponent(x,N):
    """
    Recursively prints the value of x to powers 0 to N.
    :param x: The number to raise to a power.
    :param N: The highest power to which the number should be raised.
    :return: None
    """
    if N < 0:
        pass
    else:
        test_exponent(x, N-1)
        print(exponent(x, N))


def main():
    test_fibonacci(10)
    test_factorial(10)
    test_exponent(2, 10)


main()
