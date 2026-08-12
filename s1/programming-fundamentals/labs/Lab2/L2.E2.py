date = input().split(" ")
if len(date) != 3:
    print("Invalid date")
    exit(1)

# just in case if any part is not a integer
try:
    [y, m, d] = [int(i) for i in date]
except:
    print("Invalid date")
    exit(1)


# a) if m < 3 let m = m + 12 and let y = y - 1
if m < 3:
    m = m + 12
    y = y - 1

# // for integer division as mentioned

# b) let a = 2m + 6 (m + 1) / 10
a = 2 * m + 6 * (m + 1) // 10

# c) let b = y + y/4 – y/100 + y/400
b = y + y // 4 - y // 100 + y // 400

# d) let f1 = d + a + b +1
f1 = d + a + b + 1

# e) let f = f1 mod 7
f = f1 % 7

print(f)
