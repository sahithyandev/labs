import math

try:
    inp = "48569/65711"

    inp_parts = list(map(int, inp.split("/")))
    up = inp_parts[0]
    down = inp_parts[1]

    if up >= down:
        times = up // down
        up = up % down
        if up == 0:
            print(times)
        else:
            print("%d | %d / %d" % (times, up, down))
    elif down > up:
        greatest_common_divisor = math.gcd(up, down)
        up = up // greatest_common_divisor
        down = down // greatest_common_divisor

        print("%d / %d" % (up, down))
except:
    print("Error occurred")
