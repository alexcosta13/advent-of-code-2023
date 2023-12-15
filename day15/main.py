from collections import defaultdict


def custom_hash(str):
    h = 0
    for c in str:
        h = ((h + ord(c)) * 17) % 256
    return h


def hashmap(input):
    boxes = defaultdict(list)
    steps = input.split(",")
    for s in steps:
        if s[-1] == "-":
            label = s[:-1]
            box = boxes[custom_hash(label)]
            for l, n in box:
                if l == label:
                    box.remove((label, n))
        else:
            label, num = s.split("=")
            num = int(num)
            box = boxes[custom_hash(label)]
            for i, (l, n) in enumerate(box):
                if l == label:
                    box[i] = (label, num)
                    break
            else:
                box.append((label, num))
    return sum(
        [
            (k + 1) * (i + 1) * value
            for k, box in boxes.items()
            for i, (_, value) in enumerate(box)
        ]
    )


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.read().strip()

    part1 = sum([custom_hash(line) for line in line.split(",")])
    print("First part:", part1)

    part2 = hashmap(line)
    print("Second part:", part2)
