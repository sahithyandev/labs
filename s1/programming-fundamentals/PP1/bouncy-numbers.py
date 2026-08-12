
def is_increasing(n: int):
    digits = list(str(n))
    for digit_index in range(1, len(digits)):
        if digits[digit_index - 1] > digits[digit_index]:
            return False
    return True


def is_decreasing(n: int):
    digits = list(str(n))
    for digit_index in range(1, len(digits)):
        if digits[digit_index - 1] < digits[digit_index]:
            return False
    return True


[starting, ending] = map(int, input().split())
total = 0
for n in range(starting, ending+1):
    if is_increasing(n) or is_decreasing(n):
        continue
    total += n

print(total)
