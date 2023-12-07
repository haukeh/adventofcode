from collections import defaultdict


def parse(line):
    _, nums = line.split(":")
    won, ours = [c.strip().split() for c in nums.split("|")]
    return set(map(int, won)), set(map(int, ours))


with open("input/04.txt") as f:
    cards = {
        k + 1: len(won & ours)
        for k, (won, ours) in enumerate([parse(l) for l in f.readlines()])
    }

    p1 = sum(map(lambda x: 2 ** (x - 1), filter(lambda x: x > 0, cards.values())))

    copies = defaultdict(lambda: 1)

    for num, wins in cards.items():
        for j in range(copies[num]):
            for i in range(1, wins + 1):
                n = num + i
                if n in cards:
                    copies[n] += 1

    p2 = sum(map(lambda k: copies[k], cards.keys()))

    print(p1)
    print(p2)
