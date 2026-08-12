input_strs = ["1000000", "10011"]

def compare(str1: str, str2: str):
    print("comparing", str1, str2)
    if str1 == str2:
        return True

    if "00" not in str1:
        return False

    i = str1.find("00")
    while i != -1:
        compared = compare(str1[0:i] + "1" + str1[i+2:], str2)
        if compared:
            return True
        i = str1.find("00", i+1)

    return False

print("Yes" if compare(input_strs[0], input_strs[1]) else "No")
