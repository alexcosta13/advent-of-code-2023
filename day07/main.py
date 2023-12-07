from collections import Counter
import functools

VALUES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}


def get_label(cards, part_two=False):
    counter = Counter(cards)
    if part_two:
        j = counter["J"]
        counter["J"] = 0
        counts = sorted(counter.values(), reverse=True)
        counts[0] += j
    else:
        counts = sorted(counter.values(), reverse=True)
    if counts[0] == 5 or counts[0] == 4:
        return counts[0]
    if counts[0] == 3:
        return 3.5 if counts[1] == 2 else 3
    if counts[0] == 2:
        return 2.5 if counts[1] == 2 else 2
    return 1


def transform(c, part_two=False):
    if part_two and c == "J":
        return 1
    return int(c) if c.isnumeric() else VALUES[c]


def compare(bet1, bet2, part_two=False):
    bet1 = bet1[0]
    bet2 = bet2[0]
    bet1_label = get_label(bet1, part_two)
    bet2_label = get_label(bet2, part_two)
    if bet1_label != bet2_label:
        return 1 if bet1_label > bet2_label else -1
    for x, y in zip(bet1, bet2):
        if x != y:
            return 1 if transform(x, part_two) > transform(y, part_two) else -1


def compare_two(bet1, bet2):
    return compare(bet1, bet2, True)


def get_score(bets, part_two=False):
    bets = list(map(lambda x: x.split(), bets))
    if part_two:
        bets.sort(key=functools.cmp_to_key(compare_two))
    else:
        bets.sort(key=functools.cmp_to_key(compare))
    result = 0
    for i, item in enumerate(bets):
        result += (i + 1) * int(item[1])
    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    part1 = get_score(lines.split("\n"))
    print("First part:", part1)

    part2 = get_score(lines.split("\n"), True)
    print("Second part:", part2)
