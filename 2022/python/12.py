from collections import deque
import sys


def transform(c):
    if c == 'S':
        return 1
    elif c == 'E':
        return 27
    else:
        return ord(c) - ord('a') + 1


G = [[x for x in y] for y in open("input/12_t").read().split("\n")]

for y in range(len(G)):
    for x in range(len(G[0])):
        if G[y][x] == 'S':
            S = (x, y)
        if G[y][x] == 'E':
            E = (x, y)

        G[y][x] = transform(G[y][x])

for y in G: 
    print(f'{str(y)}\n')

shortest = sys.maxsize
visited = set()

Q = deque([(S[0], S[1], 1)])
while Q:
    x, y, l = Q.popleft()

    print(f'{x} {y} {l}')

    if (x, y) == E:
        print("Found E")
        shortest = l
        break

    if (x, y) in visited:
        continue
    visited.add((x, y))

    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if (0 <= ny < len(G)) and (0 <= nx < len(G[0])):
            if (G[ny][nx] + 1 <= G[y][x]):
                Q.append((nx, ny, l + 1))

print(shortest)
