from math import sqrt


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3
    sqrtOfn = sqrt(n)
    while i <= sqrtOfn:
        if n % i == 0:
            return False
        i += 2
    return True


print(isPrime(11))


while True:
    i = int(input())
    if i < 0:
        break
    if isPrime(i):
        print('prime')
    else:
        print('non-prime')
