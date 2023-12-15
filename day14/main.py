def parse_platform(platform):
    platform_dict = dict()
    for i, line in enumerate(platform):
        for j, c in enumerate(line):
            if c in ("O", "#"):
                platform_dict[(i, j)] = c
    return platform_dict, len(platform)


# Useful to debug
def print_platform(platform, size):
    layout = [["."] * size for _ in range(size)]
    for (i, j), v in platform.items():
        layout[i][j] = v
    for line in layout:
        print("".join(line))
    print()


def tilt_north(platform, size):
    tilted_platform = dict()
    for j in range(size):
        empty_space = 0
        for i in range(size):
            if (i, j) in platform:
                if platform[(i, j)] == "O":
                    tilted_platform[(empty_space, j)] = "O"
                    empty_space += 1
                if platform[(i, j)] == "#":
                    tilted_platform[(i, j)] = "#"
                    empty_space = i + 1
    return tilted_platform


def rotate_platform(platform, size):
    return {(j, size - 1 - i): v for (i, j), v in platform.items()}


def calculate_weight(platform, size):
    return sum([size - i for (i, _), v in platform.items() if v == "O"])


def part_one(platform):
    platform, size = parse_platform(platform)
    platform = tilt_north(platform, size)
    return calculate_weight(platform, size)


def part_two(lines):
    seen_states = dict()
    platform, size = parse_platform(lines)
    i = 0
    total = 1000000000
    cycle = 0
    while i < total:
        for j in range(4):
            platform = tilt_north(platform, size)
            platform = rotate_platform(platform, size)
        i += 1
        if hash(frozenset(platform.items())) in seen_states and cycle == 0:
            cycle = i - seen_states[hash(frozenset(platform.items()))]
            i += ((total - i) // cycle) * cycle
        seen_states[hash(frozenset(platform.items()))] = i
    return calculate_weight(platform, size)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    part1 = part_one(lines.split("\n"))
    print("First part:", part1)

    part2 = part_two(lines.split("\n"))
    print("Second part:", part2)
