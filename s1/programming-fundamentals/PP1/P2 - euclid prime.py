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


n = int(input())
euclids_number = 2
total_primes_found = 1
last_checked_number = 3

while total_primes_found < n:
    if is_prime(last_checked_number):
        euclids_number *= last_checked_number
        total_primes_found += 1
    last_checked_number += 2

euclids_number += 1
print(euclids_number)
