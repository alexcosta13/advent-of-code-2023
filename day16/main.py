NEXT = {
    "RIGHT": (0, 1),
    "LEFT": (0, -1),
    "UP": (-1, 0),
    "DOWN": (1, 0),
}


def parse_grid(lines):
    grid_dict = dict()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c in ("-", "|", "/", "\\"):
                grid_dict[(i, j)] = c
    return grid_dict, len(lines)


def sum_coordinates(a, b):
    return (a[0] + b[0], a[1] + b[1])


def next_tiles(direction, current_tile, grid, size):
    x_1, y_1 = current_tile
    if x_1 >= size or y_1 >= size or x_1 < 0 or y_1 < 0:
        return []
    if current_tile not in grid:
        return [(direction, sum_coordinates(current_tile, NEXT[direction]))]
    if (direction in ("RIGHT", "LEFT") and grid[current_tile] == "-") or (
        direction in ("UP", "DOWN") and grid[current_tile] == "|"
    ):
        return [(direction, sum_coordinates(current_tile, NEXT[direction]))]
    if direction in ("RIGHT", "LEFT") and grid[current_tile] == "|":
        return [
            ("UP", sum_coordinates(current_tile, NEXT["UP"])),
            ("DOWN", sum_coordinates(current_tile, NEXT["DOWN"])),
        ]
    if direction in ("UP", "DOWN") and grid[current_tile] == "-":
        return [
            ("RIGHT", sum_coordinates(current_tile, NEXT["RIGHT"])),
            ("LEFT", sum_coordinates(current_tile, NEXT["LEFT"])),
        ]
    if (direction == "RIGHT" and grid[current_tile] == "/") or (
        direction == "LEFT" and grid[current_tile] == "\\"
    ):
        return [("UP", sum_coordinates(current_tile, NEXT["UP"]))]
    if (direction == "RIGHT" and grid[current_tile] == "\\") or (
        direction == "LEFT" and grid[current_tile] == "/"
    ):
        return [("DOWN", sum_coordinates(current_tile, NEXT["DOWN"]))]
    if (direction == "UP" and grid[current_tile] == "\\") or (
        direction == "DOWN" and grid[current_tile] == "/"
    ):
        return [("LEFT", sum_coordinates(current_tile, NEXT["LEFT"]))]
    if (direction == "UP" and grid[current_tile] == "/") or (
        direction == "DOWN" and grid[current_tile] == "\\"
    ):
        return [("RIGHT", sum_coordinates(current_tile, NEXT["RIGHT"]))]
    print("OOOOOUT", direction, current_tile, grid[current_tile])


def light(grid, size, start=("RIGHT", (0, 0))):
    bright_tiles = set()
    todo = [start]
    while len(todo) > 0:
        direction, tile = todo.pop()
        if (direction, tile) in bright_tiles:
            continue
        bright_tiles.add((direction, tile))
        todo += next_tiles(direction, tile, grid, size)
    return len(
        {
            (a, b)
            for _, (a, b) in bright_tiles
            if a < size and b < size and a >= 0 and b >= 0
        }
    )


def max_energy(grid, size):
    return max(
        [
            max(
                light(grid, size, ("DOWN", (0, i))),
                light(grid, size, ("UP", (size - 1, i))),
                light(grid, size, ("RIGHT", (i, 0))),
                light(grid, size, ("LEFT", (i, size - 1))),
            )
            for i in range(size)
        ]
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    grid, size = parse_grid(lines.split("\n"))

    part1 = light(grid, size)
    print("First part:", part1)

    part2 = max_energy(grid, size)
    print("Second part:", part2)
