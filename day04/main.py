# PART 1
def matching_numbers(line):
    _, numbers = line.split(":")
    winning_numbers, card_numbers = list(
        map(lambda x: set(x.split()), numbers.split("|"))
    )
    correct_numbers = winning_numbers & card_numbers
    if len(correct_numbers) < 2:
        return len(correct_numbers)
    else:
        return 2 ** (len(correct_numbers) - 1)


# PART 2
def get_cards(line):
    id, numbers = line.split(":")
    id = int(id.split()[1])
    winning_numbers, card_numbers = list(
        map(lambda x: set(x.split()), numbers.split("|"))
    )
    correct_numbers = winning_numbers & card_numbers
    return id, list((range(id + 1, id + len(correct_numbers) + 1)))


def count_cards(lines):
    results = dict()
    for line in lines.split("\n")[::-1]:
        count = 1
        id, extra_cards = get_cards(line)
        for card in extra_cards:
            count += results[card]
        results[id] = count
    return results


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().strip()

    result = [matching_numbers(line) for line in lines.split("\n")]

    part1 = sum(result)
    print("First part:", part1)

    cards = count_cards(lines)

    part2 = sum(cards.values())
    print("Second part:", part2)
