from time import localtime
current_time = localtime()
time = f"{str(current_time.tm_hour).rjust(2,'0')}.{str(current_time.tm_min).rjust(2,'0')}am"

hours,minutes = list(map(int, time[0:-2].split(".")))

if time [-2] == "p":
    hours += 12

def convert_to_7_segments(n: str):
    match n:
        case "0":
            return [
                " _ ",
                "| |",
                "   ",
                "| |",
                " _ ",
            ]
        case "1":
            return [
                "   ",
                "  |",
                "   ",
                "  |",
                "   ",
            ]
        case "2":
            return [
                " _ ",
                "  |",
                " _ ",
                "|  ",
                " _ ",
            ]
        case "3":
            return [
                " _ ",
                "  |",
                " _ ",
                "  |",
                " _ ",
            ]
        case "4":
            return [
                "   ",
                "| |",
                " _ ",
                "  |",
                "   ",
            ]
        case "5":
            return [
                " _ ",
                "|  ",
                " _ ",
                "  |",
                " _ ",
            ]
        case "6":
            return [
                " _ ",
                "|  ",
                " _ ",
                "| |",
                " _ ",
            ]
        case "7":
            return [
                " _ ",
                "  |",
                "   ",
                "  |",
                "   ",
            ]
        case "8":
            return [
                " _ ",
                "| |",
                " _ ",
                "| |",
                " _ ",
            ]
        case "9":
            return [
                " _ ",
                "| |",
                " _ ",
                "  |",
                " _ ",
            ]
        case ":":
            return [
                "   ",
                " . ",
                "   ",
                " . ",
                "   ",
            ]
        case _:
            raise ValueError

print(hours, minutes)

lines: list[str] = []

for digit in str(hours).rjust(2,"0") + ":" + str(minutes).rjust(2,"0"):
    _lines = convert_to_7_segments(digit)
    if len(lines) == 0:
        lines = _lines
        continue

    for line in range(len(_lines)):
        lines[line] += " " + _lines[line]


for line in lines:
    print(line)
