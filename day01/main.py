NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_number(line, part_two=False):
    if line[0].isnumeric():
        return int(line[0])
    if not part_two:
        return
    for n in NUMBERS.keys():
        if line.startswith(n):
            return NUMBERS[n]


def get_number_from_line(line, part_two=False):
    for i in range(len(line)):
        a = find_number(line[i:], part_two)
        if a:
            break
    for i in range(len(line) - 1, -1, -1):
        b = find_number(line[i:], part_two)
        if b:
            break

    return 10 * a + b


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    calibration_values_one = [get_number_from_line(line) for line in lines.split("\n")]

    calibration_values_two = [
        get_number_from_line(line, part_two=True) for line in lines.split("\n")
    ]

    part1 = sum(calibration_values_one)
    print("First part:", part1)

    part2 = sum(calibration_values_two)
    print("Second part:", part2)
