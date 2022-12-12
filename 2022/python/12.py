import sys
from collections import deque


def transform(c):
    if c == 'S':
        return 1
    elif c == 'E':
        return 27
    else:
        return ord(c) - ord('a') + 1

G = [[x for x in y] for y in open("input/12").read().split("\n")]

for y in range(len(G)):
    for x in range(len(G[0])):
        if G[y][x] == 'S':
            S = (x, y)
        if G[y][x] == 'E':
            E = (x, y)

        G[y][x] = transform(G[y][x])

def shortest_path(start):
    global G
    
    q = deque([(start[0], start[1], 0)])
    visited = set()

    while q:
        x, y, l = q.popleft()
        if (x, y) == E:
            return l
        
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            yy = y + dy
            xx = x + dx        
            if (0 <= yy < len(G)) and (0 <= xx < len(G[0])):
                if (G[yy][xx] <= G[y][x]+1):
                    q.append((xx, yy, l + 1))
    

starts = []
for y in range(len(G)):
    for x in range(len(G[0])):
        if G[y][x] == 1:
            starts.append((x, y))

p1 = shortest_path(S)
p2 = min(filter(lambda x: x, [shortest_path(s) for s in starts]))

print(p1)
print(p2)

