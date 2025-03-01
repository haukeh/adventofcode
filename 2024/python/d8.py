from collections import defaultdict
import itertools


G = {
    (x, y): char
    for y, line in enumerate(open("../input/d8.txt").readlines())
    for x, char in enumerate(line.strip())
}


antennas = defaultdict(list)
for pos, c in G.items():
    if c != ".":
        antennas[c].append(pos)


def p1():
    antinodes = set()
    for posis in antennas.values():
        pairs = list(itertools.combinations(posis, 2))
        for (ax, ay), (bx, by) in pairs:
            dx = ax - bx
            dy = ay - by
            anti_a = (ax + dx, ay + dy)
            anti_b = (bx - dx, by - dy)
            if anti_a in G:
                antinodes.add(anti_a)
            if anti_b in G:
                antinodes.add(anti_b)

    return len(antinodes)


def p2():
    antinodes = set()
    for posis in antennas.values():
        antinodes.update(posis)
        pairs = list(itertools.combinations(posis, 2))
        for (ax, ay), (bx, by) in pairs:
            dx = ax - bx
            dy = ay - by
            anti_a = (ax + dx, ay + dy)
            anti_b = (bx - dx, by - dy)
            while anti_a in G:
                antinodes.add(anti_a)
                anti_a = (anti_a[0] + dx, anti_a[1] + dy)
            while anti_b in G:
                antinodes.add(anti_b)
                anti_b = (anti_b[0] - dx, anti_b[1] - dy)

    return len(antinodes)


print(p1())
print(p2())
