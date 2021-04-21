def factorialA(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def factorialB(n):
    if n == 1:
        return n
    else:
        return n * factorialB(n - 1)
