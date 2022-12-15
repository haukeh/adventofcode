import itertools
from collections import defaultdict
from copy import deepcopy


def parse(items):
    res = []
    for item in items:
        x, y = item.strip().split(",")
        res.append((int(x), int(y)))
    return res


def line(a, b):
    (ax, ay) = a
    (bx, by) = b
    res = []
    if ax == bx:
        for y in range(min(ay, by), max(ay, by) + 1):
            res.append((ax, y))
    if ay == by:
        for x in range(min(ax, bx), max(ax, bx) + 1):
            res.append((x, ay))
    return res


def fall(g, start, max_y, p1=True):
    cnt = 0
    pos = start
    while pos[1] < max_y:
        next = (pos[0], pos[1] + 1)
        blocked = g[next]

        if blocked:
            botleft = (pos[0] - 1, pos[1] + 1)
            botright = (pos[0] + 1, pos[1] + 1)
            if not g[botleft]:
                return fall(g, botleft, max_y, p1)
            elif not g[botright]:
                return fall(g, botright, max_y, p1)
            else:
                return pos
        else:
            pos = next
            cnt += 1

    return None if p1 else (pos[0], max_y - 1)


items = [parse(line.split("->")) for line in open("input/14").read().split("\n")]

G = defaultdict(bool)
max_y = 0

for item in items:
    for (a, b) in itertools.pairwise(item):
        max_y = max(max_y, a[1], b[1])
        for p in line(a, b):
            G[p] = True

G2 = deepcopy(G)


def run(g, max_y, p1=True):
    falling = True
    units = 0

    while falling:
        end_pos = fall(g, (500, 0), max_y, p1)
        if not p1 and end_pos == (500, 0):
            falling = False
        elif p1 and end_pos == None:
            falling = False
        else:
            g[end_pos] = True
            units += 1

    return units


p1 = run(G, max_y)
p2 = run(G2, max_y + 2, p1=False) + 1

print(p1)
print(p2)
