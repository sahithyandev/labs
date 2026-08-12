message = input("Enter message: ")
base = int(input("Enter base: "))

encryptedMessage = ""

for i in message:
    ordinal = ord(i)

    in_base = ""
    if ordinal == 0:
        in_base = "0"
    else:
        quotient = ordinal
        while quotient != 0:
            in_base = str(quotient % base) + in_base
            quotient = quotient // base

    encryptedMessage = encryptedMessage+in_base


print(encryptedMessage)
