message = input("Enter message: ")
base = int(input())

encryptedMessage = ""


def numberToBase(n, b):
    if n == 0:
        return "0"
    digits = ""
    while n:
        digits += str(int(n % b))
        n //= b
    return digits[::-1]


for i in message:
    ordinal = ord(i)
    encryptedMessage += numberToBase(ordinal, base)

for i in range(0, len(message)+1):
    letter = message[i]
    ordinal = ord(letter)
    encryptedMessage += numberToBase(ordinal, base)

print(encryptedMessage)
