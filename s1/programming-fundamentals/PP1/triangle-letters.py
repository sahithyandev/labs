from string import ascii_uppercase

letters = ascii_uppercase
letter = "H"

n = letters.index(letter)
size = 2 * n + 1

for i in range(0, size):
    _i = i if i <= n else (size - i - 1)
    print(
        (
            letters[0:(_i)] +
            letters[_i] +
            letters[0:(_i)][::-1]
        ).center(size)
    )
