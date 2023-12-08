import math


def move(instructions, map, pos="AAA"):
    i = 0
    # assumes that the first XXZ that we encounter in part one is ZZZ, which in my cas is true
    while pos[2] != "Z":
        pos = map[pos][0] if instructions[i % len(instructions)] == "L" else map[pos][1]
        i += 1
    return i


def ghosts(instructions, map):
    pos = [k for k in map.keys() if k[2] == "A"]
    moves = [move(instructions, map, p) for p in pos]
    return math.lcm(*moves)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    instructions, map = lines.split("\n\n")
    map = {m[0:3]: (m[7:10], m[12:15]) for m in map.split("\n")}

    part1 = move(instructions, map)
    print("First part:", part1)

    part2 = ghosts(instructions, map)
    print("Second part:", part2)
