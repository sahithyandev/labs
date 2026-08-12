from math import sqrt

user_input = int(input("Enter number: "))


def is_prime(n):
    """
    Find if a number n is a prime number or not
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


factors = {}

n = user_input
while n != 1:
    for i in range(2, n + 1):
        if n % i != 0:
            continue
        if is_prime(i):
            str_i = str(i)
            if str_i in factors:
                factors[str_i] += 1
            else:
                factors[str_i] = 1
        n = int(n / i)
        break

total_factors_count = len(factors)
i = 0
for factor in factors:
    i += 1
    count = factors[factor]
    if count == 1:
        print(factor, end="")
    else:
        print(f"{factor}^{count}", end="")
    if total_factors_count != i:
        print(" x ", end="")
    else:
        print()
