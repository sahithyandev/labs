inp = "48569/65711"


def parse_input(input_string: str):
    parts = input_string.split("/")
    if len(parts) != 2:
        print("Invalid input")
        exit()
    try:
        return list(map(int, parts))
    except:
        print("Invalid input")
        exit()


def gcd(a: int, b: int):
    if a == b:
        return a
    if a > b:
        return gcd(a-b, b)
    if b > a:
        return gcd(a, b-a)


[up, down] = parse_input(inp)
if up % down == 0:
    print(f"{up//down}")
    exit(0)


times = 0
if up > down:
    times = up // down
    up = up % down

common_divisor = gcd(up, down)

if times == 0:
    print(f"{up//common_divisor}/{down//common_divisor}")
else:
    print(f"{times}|{up//common_divisor}/{down//common_divisor}")
