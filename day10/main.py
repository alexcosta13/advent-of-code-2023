START = (21, 29)
START_EXAMPLE = (0, 4)

PIPES = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}


def next_postition(last_position, current_position, grid):
    pos = PIPES[grid[current_position[0]][current_position[1]]]
    pos = [(current_position[0] + a, current_position[1] + b) for a, b in pos]
    return pos[0] if pos[0] != last_position else pos[1]


def count_segments_down(pipe):
    total = 0
    for p in pipe:
        if p == "|":
            continue
        elif p == "-":
            total += 1
        elif p in ("F", "7"):
            last = p
        elif p == "L":
            total += 1 if last == "7" else 0
        elif p == "J":
            total += 1 if last == "F" else 0
    return total


def count_segments_right(pipe):
    total = 0
    for p in pipe:
        if p == "-":
            continue
        if p == "|":
            total += 1
        if p in ("L", "F"):
            last = p
        elif p == "7":
            total += 1 if last == "L" else 0
        elif p == "J":
            total += 1 if last == "F" else 0
    return total


def in_loop(i, j, pipe):
    if (i, j) in pipe:
        return False
    horizontal = [pipe[(i, k)] for k in range(0, j) if (i, k) in pipe]
    r = count_segments_right(horizontal)
    vertical = [pipe[(k, 0)] for k in range(0, i) if (k, 0) in pipe]
    d = count_segments_down(vertical)
    return (d + r) % 2


def solve(grid, starting_position, part_two=False):
    i = 0
    previous_position = (0, 0)
    current_position = starting_position
    pipe = dict()
    while True:
        aux = next_postition(previous_position, current_position, grid)
        previous_position = current_position
        current_position = aux
        pipe[current_position] = grid[current_position[0]][current_position[1]]
        i += 1
        if current_position == starting_position:
            break
    if not part_two:
        return i // 2
    return sum(
        [
            1
            for i in range(len(grid))
            for j in range(len(grid[0]))
            if in_loop(i, j, pipe)
        ]
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    part1 = solve(lines.split("\n"), START)
    print("First part:", part1)

    part2 = solve(lines.split("\n"), START, part_two=True)
    print("Second part:", part2)
