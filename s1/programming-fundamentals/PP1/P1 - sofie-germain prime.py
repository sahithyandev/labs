from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


starting = int(input())
ending = int(input())

sum_of_those = 0

for n in range(starting, ending+1):
    if not is_prime(n) or not is_prime(2 * n + 1):
        continue
    print(n)
    sum_of_those += n

print(sum_of_those)
