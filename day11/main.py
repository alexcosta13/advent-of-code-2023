def adjust_universe(universe):
    empty_rows = []
    empty_columns = []
    for i, line in enumerate(universe):
        if line == "." * len(line):
            empty_rows.append(i)
    for i, line in enumerate(list(zip(*universe))):
        if "".join(line) == "." * len(line):
            empty_columns.append(i)
    return empty_rows, empty_columns


def get_galaxies(universe):
    for i, line in enumerate(universe):
        for j, char in enumerate(line):
            if char == "#":
                yield ((i, j))


def calculate_distances(galaxies, empty_rows, empty_columns, extra_space=1):
    galaxies = list(galaxies)
    for i, a in enumerate(galaxies):
        for b in galaxies[i + 1 :]:
            x = len(
                [i for i in range(min(a[0], b[0]), max(a[0], b[0])) if i in empty_rows]
            ) + len(
                [
                    i
                    for i in range(min(a[1], b[1]), max(a[1], b[1]))
                    if i in empty_columns
                ]
            )
            yield abs(a[0] - b[0]) + abs(a[1] - b[1]) + (extra_space) * x


def solve(universe, extra_space=1):
    empty_rows, empty_columns = adjust_universe(universe)
    galaxies = get_galaxies(universe)
    return calculate_distances(galaxies, empty_rows, empty_columns, extra_space)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    result = solve(lines.split("\n"))

    part1 = sum(result)
    print("First part:", part1)

    result = solve(lines.split("\n"), 1000000 - 1)

    part2 = sum(result)
    print("Second part:", part2)
