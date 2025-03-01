import heapq


G = {
    (x, y): c
    for y, line in enumerate(open("../input/d16.txt").read().split("\n"))
    for x, c in enumerate(line)
}

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def shortest_path(start, end):
    Q = []
    seen = set()
    heapq.heappush(Q, (0, 0, start))

    while Q:
        cost, d, pos = heapq.heappop(Q)
        seen.add((d, pos))
        
        if pos == end:
            return cost

        dx, dy = DIR[d]
        for next in [
            (cost + 1, d, (pos[0] + dx, pos[1] + dy)),
            (cost + 1000, (d + 1) % 4, pos),
            (cost + 1000, (d - 1) % 4, pos),
        ]:
            _, d, pos = next
            if G.get(pos) != "#" and (d, pos) not in seen:
                heapq.heappush(Q, next)


for pos, c in G.items():
    if c == "S":
        start = pos
    if c == "E":
        end = pos

p1 = shortest_path(start, end)
print(p1)
