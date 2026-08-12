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


if __name__ == "__main__":
    print(is_prime(192))
