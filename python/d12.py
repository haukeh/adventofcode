from collections import defaultdict
import sys

sys.setrecursionlimit(100000)

lines = enumerate(open("../input/d12.txt").readlines())

G = {(x, y): c for y, line in lines for x, c in enumerate(line.strip())}
DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]


pos_to_num = {}


def fill_plots(pos, v, n):
    value = G.get(pos)
    if value is not None:
        if pos in pos_to_num:
            return

        if value == v:
            pos_to_num[pos] = n
            for dx, dy in DIR:
                fill_plots((pos[0] + dx, pos[1] + dy), v, n)


# https://www.reddit.com/r/adventofcode/comments/1hcf16m/2024_day_12_everyone_must_be_hating_today_so_here/
def num_corners(pos):
    x, y = pos
    value = pos_to_num.get(pos)
    right = pos_to_num.get((x + 1, y))
    bottom = pos_to_num.get((x, y + 1))
    left = pos_to_num.get((x - 1, y))
    top = pos_to_num.get((x, y - 1))

    outer_corners = 0
    inner_corners = 0

    if right != value and top != value:
        outer_corners += 1
    if bottom != value and right != value:
        outer_corners += 1
    if bottom != value and left != value:
        outer_corners += 1
    if top != value and left != value:
        outer_corners += 1

    if pos_to_num.get((x + 1, y - 1)) != value and right == value and top == value:
        inner_corners += 1
    if pos_to_num.get((x + 1, y + 1)) != value and right == value and bottom == value:
        inner_corners += 1
    if pos_to_num.get((x - 1, y + 1)) != value and left == value and bottom == value:
        inner_corners += 1
    if pos_to_num.get((x - 1, y - 1)) != value and left == value and top == value:
        inner_corners += 1

    return outer_corners + inner_corners


plot_num = 0
for pos, type in G.items():
    if pos not in pos_to_num:
        fill_plots(pos, type, plot_num)
        plot_num += 1

num_to_pos = defaultdict(set)
for k, v in pos_to_num.items():
    num_to_pos[v].add(k)

p1 = 0
p2 = 0

for _, positions in num_to_pos.items():
    area = len(positions)
    perimeter = []
    sides = 0

    for x, y in positions:
        for dx, dy in DIR:
            neighbour = (x + dx, y + dy)
            if neighbour not in positions or neighbour not in G:
                perimeter.append((x, y))

        sides += num_corners((x, y))

    # print(f"{G[next(iter(posis))]}: {area} * {sides}")

    p1 += area * len(perimeter)
    p2 += area * sides


print(p1)
print(p2)
