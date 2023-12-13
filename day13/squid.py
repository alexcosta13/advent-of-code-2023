import math

for n in range(2, 19):
    print(f"Probability fo player {n}")
    print(sum([((1 / 2) ** 18) * math.comb(i - 1, n - 2) for i in range(n, 19)]))
