def find_simmetry(pattern, smudge=0):
    for i, (a, b) in enumerate(zip(pattern[:-1], pattern[1:])):
        mistakes = sum([0 if x == y else 1 for x, y in zip(a, b)])
        if mistakes <= smudge:
            for j in range(1, min(i + 1, len(pattern) - i - 1)):
                mistakes += sum(
                    [
                        0 if x == y else 1
                        for x, y in zip(pattern[i - j], pattern[i + 1 + j])
                    ]
                )
                if mistakes > smudge:
                    break
            else:
                if mistakes == smudge:
                    return 100 * (i + 1)
    pattern = list(map(list, zip(*pattern)))
    for i, (a, b) in enumerate(zip(pattern[:-1], pattern[1:])):
        mistakes = sum([0 if x == y else 1 for x, y in zip(a, b)])
        if mistakes <= smudge:
            for j in range(1, min(i + 1, len(pattern) - i - 1)):
                mistakes += sum(
                    [
                        0 if x == y else 1
                        for x, y in zip(pattern[i - j], pattern[i + 1 + j])
                    ]
                )
                if mistakes > smudge:
                    break
            else:
                if mistakes == smudge:
                    return i + 1
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    result = [find_simmetry(pattern.split("\n")) for pattern in lines.split("\n\n")]
    part1 = sum(result)
    print("First part:", part1)

    result = [
        find_simmetry(pattern.split("\n"), smudge=1) for pattern in lines.split("\n\n")
    ]
    part2 = sum(result)
    print("Second part:", part2)
