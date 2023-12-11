def solve(line, beginning=False):
    numbers = list(map(int, line.split()))
    acc = [numbers[0 if beginning else -1]]
    while True:
        numbers = [b - a for a, b in zip(numbers[:-1], numbers[1:])]
        acc.append(numbers[0 if beginning else -1])
        if len([x for x in numbers if x != 0]) == 0:
            break
    if not beginning:
        return sum(acc)
    result = 0
    for a in acc[::-1]:
        result = a - result
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    result = [solve(line) for line in lines.split("\n")]

    part1 = sum(result)
    print("First part:", part1)

    result = [solve(line, beginning=True) for line in lines.split("\n")]

    part2 = sum(result)
    print("Second part:", part2)
