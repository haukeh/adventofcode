from collections import defaultdict
import heapq


G = defaultdict(lambda: ".")
DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N = 71


def shortest_path(start, end):
    Q = []
    shortest = defaultdict(lambda: float("inf"))
    shortest[start] = 0
    heapq.heappush(Q, (0, start))

    while Q:
        steps, pos = heapq.heappop(Q)

        if pos == end:
            return steps

        for dx, dy in DIR:
            next = (pos[0] + dx, pos[1] + dy)
            x, y = next
            nn = G[next]
            if x in range(N) and y in range(N) and nn == ".":
                if steps + 1 < shortest[next]:
                    shortest[next] = steps + 1
                    heapq.heappush(Q, (steps + 1, next))


i = 0
for x, y in list(
    map(lambda x: map(int, x.split(",")), open("../input/d18.txt").readlines())
):
    i += 1
    G[x, y] = "#"
    res = shortest_path((0, 0), (70, 70))

    if i == 1024:
        print(res)  # p1

    if res is None:
        print([x, y])  # p2
        break
