import re

COLOR_MAX = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def get_id_from_valid_game(line):
    info = re.findall("\d+\s\w+", line)
    for item in info:
        num, color = item.split()
        if int(num) > COLOR_MAX[color]:
            return False
    return True


def get_power(line):
    info = re.findall("\d+\s\w+", line)
    color_min = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for item in info:
        num, color = item.split()
        color_min[color] = max(color_min[color], int(num))
    return color_min["red"] * color_min["green"] * color_min["blue"]


if __name__ == "__main__":
    with open("example.txt") as f:
        lines = f.read().strip()

    valid_ids = [
        id + 1
        for id, line in enumerate(lines.split("\n"))
        if get_id_from_valid_game(line)
    ]

    powers = [get_power(line) for line in lines.split("\n")]

    part1 = sum(valid_ids)
    print("First part:", part1)

    part2 = sum(powers)
    print("Second part:", part2)
