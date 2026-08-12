from math import sqrt

[a, b] = map(int, input().split())


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def is_palindromic(n: int):
    return str(n) == str(n)[::-1]


sss = 0
for n in range(a, b+1):
    if not is_palindromic(n):
        continue
    if is_prime(n):
        print(n)
        sss += n
    else:
        sqrt_n = sqrt(n)
        if int(sqrt_n) == sqrt_n:
            print(n)
            sss += n

# print(sss)
