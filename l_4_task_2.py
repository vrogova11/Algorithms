def prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        num_test = [num for i in primes if num % i == 0]
        primes += [] if num_test else [num]
        num += 1
    rez = primes[-1]
    return rez


print(prime(12))


def sieve(n):
    a = [0] * (n * 10)
    for i in range(n * 10):
        a[i] = i
    a[1] = 0
    m = 2
    while m < n * 10:
        if a[m] != 0:
            j = m * 2
            while j < n * 10:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    return b[n - 1]


print(sieve(12))
