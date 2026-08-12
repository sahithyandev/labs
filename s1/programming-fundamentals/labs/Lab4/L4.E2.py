def isAbundantNumber(n):
    sumOfProperDivisors = 0
    for i in range(2, n):
        if n % i == 0:
            sumOfProperDivisors += i
        if sumOfProperDivisors > n:
            return True
    return False


n = int(input("Input number: "))
if n < 2:
    print("Invalid Input")
    exit(1)

numberOfAbundantNumbers = 0
for i in range(2, n+1):
    if isAbundantNumber(i):
        numberOfAbundantNumbers += 1

print(f"Number of abundant numbers from 1 to {n} is {numberOfAbundantNumbers}")
