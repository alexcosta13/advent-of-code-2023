def parse_maps(maps):
    return [list(map(int, m.split())) for m in maps]


def converter(seed, maps):
    for m in maps:
        i, j, s = m
        if seed >= j and seed < j + s:
            return seed + i - j
    return seed


def remap(groups, m):
    transformed = []
    for line in m:
        original = []
        for group in groups:
            a, b = group
            i, j, s = line
            k = j + s - 1
            l = i + s - 1
            if k < a or j > b:
                original.append((a, b))
            elif j <= a and a <= k < b:
                original.append((k + 1, b))
                transformed.append((i + a - j, l))
            elif j > a and k < b:
                original.append((a, j - 1))
                transformed.append((i, l))
                original.append((k + 1, b))
            elif a < j <= b and k >= b:
                original.append((a, j - 1))
                transformed.append((i, i + b - j))
            elif j <= a and k >= b:
                transformed.append((i + a - j, i + b - j))
            else:
                raise NotImplemented
        groups = original.copy()
    return groups + transformed


def find_location(lines, part_two=False):
    seeds = list(map(int, lines.split("\n")[0].split()[1:]))
    maps = [parse_maps(maps.split("\n")[1:]) for maps in lines.split("\n\n")[1:]]
    if part_two:
        seeds = [
            (seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)
        ]
        for m in maps:
            seeds = remap(seeds, m)
        return seeds

    result = []
    for seed in seeds:
        for m in maps:
            seed = converter(seed, m)
        result.append(seed)
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    part1 = min(find_location(lines))
    print("First part:", part1)

    part2 = min(find_location(lines, True), key=lambda x: x[0])[0]
    print("Second part:", part2)
