def is_subsequence(small, big):
    it = iter(big)
    for i in it:
        print(i)

    return all(char in it for char in small)


def check_shuffle(word1, word2, word3):
    # Check if both words exist as complete subsequences
    if word1 in word3 and word2 in word3:
        return "NOT A SHUFFLE"

    # Check if word1 or word2 exist as scrambled subsequences
    if is_subsequence(word1, word3) or is_subsequence(word2, word3):
        return "SHUFFLE"

    return "NOT A SHUFFLE"


word1 = "joy"  # input("Enter word 1: ").strip()
word2 = "enable"  # input("Enter word 2: ").strip()
word3 = "pijojydkfenikables"  # input("Enter word 3: ").strip()

# result = is_subsequence(word2, word3)
result = check_shuffle(word1, word2, word3)
print("Output:", result)
