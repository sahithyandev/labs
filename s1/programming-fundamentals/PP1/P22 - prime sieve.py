n = int(input())

sieve = list(range(2, n))
primes = []

while len(sieve) > 0:
    i = sieve.pop(0)
    primes.append(i)
    print("prime", i)

    j = 0
    while j < len(sieve):
        if sieve[j] % i != 0:
            j += 1
            continue
        sieve.pop(j)
    print("ppp", sieve)

print(primes)
