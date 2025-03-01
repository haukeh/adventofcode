from collections import Counter


def run(iters):
    stones = Counter([int(n) for n in open("../input/d11.txt").read().split()])

    for _ in range(iters):
        counts = Counter()

        for n, cnt in stones.items():
            if n == 0:
                counts[1] += cnt
            else:
                s = str(n)
                if len(s) % 2 == 0:
                    mid = len(s) // 2
                    a, b = int(s[:mid]), int(s[mid:])
                    counts[a] += cnt
                    counts[b] += cnt
                else:
                    counts[n * 2024] += cnt

        stones = counts

    return sum(counts.values())


p1 = run(25)
p2 = run(75)

print(p1)
print(p2)
