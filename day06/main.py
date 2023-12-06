import math


def calculate(time, distance):
    for t, d in zip(time, distance):
        counter = 0
        for i in range(t):
            if (t - i) * i > d:
                counter += 1
        yield counter


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip().splitlines()

    # One liner that works, but keeping two lines for readability
    # time, distance = list(map(lambda line: list(map(int, line.split()[1:])), lines))
    time = list(map(int, lines[0].split()[1:]))
    distance = list(map(int, lines[1].split()[1:]))

    part1 = math.prod(calculate(time, distance))
    print("First part:", part1)

    # I just changed the input file first, and then built this solution
    time = [int("".join(lines[0].split()[1:]))]
    distance = [int("".join(lines[1].split()[1:]))]
    part2 = list(calculate(time, distance))[0]
    print("Second part:", part2)
