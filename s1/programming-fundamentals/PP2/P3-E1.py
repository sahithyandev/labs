males=[0]
def hofstadter_male(n: int):
    if len(males) > n:
        return males[n]

    if n == 0:
        return 0
    x = n - hofstadter_female(hofstadter_male(n-1))
    males.append(x)
    return x

females = [1]
def hofstadter_female(n: int):
    if len(females) > n:
        return females[n]
    if n == 0:
        return 1
    x= n - hofstadter_male(hofstadter_female(n-1))
    females.append(x)
    return x


for i in range(1001):
    print(f"{i}: F={hofstadter_female(i)} M={hofstadter_male(i)}")
