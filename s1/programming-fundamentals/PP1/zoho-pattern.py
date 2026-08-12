n = 6

rows = []

for i in range(1, n * (n + 1) // 2 + 1):
    _row = []
    if i <= n:
        _row.append(i)
        rows.append(_row)
    else:
        rows[(i % n) - 1].append(i)

print(rows)
