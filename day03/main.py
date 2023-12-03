import math


# PART 1
def check_validity(i, j, lines):
    if not lines[max(0, i - 1)][j].isnumeric() and lines[max(0, i - 1)][j] != ".":
        return True
    if (
        not lines[min(i + 1, len(lines) - 1)][j].isnumeric()
        and lines[min(i + 1, len(lines) - 1)][j] != "."
    ):
        return True
    if not lines[i][j].isnumeric() and lines[i][j] != ".":
        return True
    return False


def get_part_numbers(lines):
    numbers = []
    for i, line in enumerate(lines):
        num = 0
        valid = False
        for j, c in enumerate(line):
            if c.isnumeric():
                num = 10 * num + int(c)
                valid = valid or check_validity(i, j, lines)
                valid = valid or check_validity(i, max(0, j - 1), lines)
            elif num != 0:
                valid = valid or check_validity(i, j, lines)
                if valid:
                    numbers.append(num)
                num = 0
                valid = False
        valid = valid or check_validity(i, len(lines[0]) - 1, lines)
        if valid:
            numbers.append(num)
        num = 0
        valid = False

    return numbers


# PART 2
def parse(lines):
    numbers = dict()
    symbols = set()
    for i, line in enumerate(lines):
        num = 0
        acc = set()
        for j, c in enumerate(line):
            if c == "*":
                symbols.add((i, j))
            if not c.isnumeric() and num > 0:
                for pos in acc:
                    numbers[pos] = num
                acc = set()
                num = 0
            elif c.isnumeric():
                num = 10 * num + int(c)
                acc.add((i, j))
        if num > 0:
            for pos in acc:
                numbers[pos] = num
            acc = set()
            num = 0
    return numbers, symbols


def adjacent_positions(i, j):
    return [(a, b) for a in range(i - 1, i + 2) for b in range(j - 1, j + 2)]


def get_gear_ratio(numbers, symbols):
    for symbol in symbols:
        nums = set(numbers[s] for s in adjacent_positions(*symbol) if s in numbers)
        if len(nums) == 2:
            yield math.prod(nums)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    lines = lines.split("\n")

    part1 = sum(get_part_numbers(lines))
    print("First part:", part1)

    numbers, symbols = parse(lines)
    part2 = sum(get_gear_ratio(numbers, symbols))
    print("Second part:", part2)
