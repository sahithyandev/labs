n = 3
digits = ["8", "5", "1", "2", "3"]


def join_as_strings(items: list[list[str]]):
    return ["".join(item) for item in items]


def permute(items: list[str]):
    if len(items) == 1:
        return items

    _d = []
    for item in range(len(items)):
        items_except_one = items[0:item]
        items_except_one.extend(items[item+1:])

        permutated = permute(items_except_one)
        for i in permutated:
            iterated = [items[item]]
            iterated.extend(i)
            _d.append(iterated)

    return _d


permutations = join_as_strings(permute(digits))
permutations.sort()

for i in range(n):
    print(permutations[i])

print(permutations[len(permutations)-1])
