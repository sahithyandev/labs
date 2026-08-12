d = [8, 9]


def increment(num: list[int]):
    carry = 0
    num.insert(0, 0)
    for i in range(len(num)-1, -1, -1):
        if i == len(num) - 1:
            num[i] += 1
        if carry != 0:
            num[i] += carry
            carry = 0
        if num[i] >= 10:
            num[i] -= 10
            carry = 1
        if carry == 0:
            break
    while num[0] == 0:
        num.pop(0)


increment(d)
print(d)
