from functools import cache


def unfold_line(line):
    springs, groups = line.split()
    springs = ((springs + "?") * 5)[:-1]
    groups = ((groups + ",") * 5)[:-1]
    return " ".join([springs, groups])


@cache
def get_possibilities(line, acc, result):
    if len(line) == 0:
        if acc == 0 and len(result) == 0:
            return 1
        if len(result) == 1 and acc == result[0]:
            return 1
        return 0
    if line[0] == "#":
        return get_possibilities(line[1:], acc + 1, result)
    if line[0] == "?":
        return get_possibilities("." + line[1:], acc, result) + get_possibilities(
            "#" + line[1:], acc, result
        )
    # line[0] == '.':
    if acc == 0:
        return get_possibilities(line[1:], acc, result)
    if acc > 0:
        if len(result) == 0:
            return 0
        elif acc == result[0]:
            return get_possibilities(line[1:], 0, result[1:])
        return 0


def solve(line, part_two=False):
    if part_two:
        line = unfold_line(line)
    springs, groups = line.split()
    groups = tuple(map(int, groups.split(",")))
    return get_possibilities(springs, 0, groups)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    part1 = sum([solve(line) for line in lines.split("\n")])
    print("First part:", part1)

    part2 = sum([solve(line, True) for line in lines.split("\n")])
    print("Second part:", part2)
