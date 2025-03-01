from collections import defaultdict
import networkx

pairs = [line.split("-") for line in open("../input/d23.txt").read().split("\n")]

G = defaultdict(set)

for a, b in pairs:
    G[a].add(b)
    G[b].add(a)

threes = set()
for a in G:
    for b in G:
        if b > a:
            continue
        for c in G:
            if c > b:
                continue
            if a in G[b] and a in G[c] and b in G[c]:
                threes.add(frozenset({a, b, c}))


NG = networkx.Graph(G)
max_clique = []
for c in networkx.find_cliques(NG):
    if len(c) > len(max_clique):
        max_clique = c

p1 = len(list(filter(lambda s: any(x.startswith("t") for x in s), threes)))
p2 = ",".join(sorted(max_clique))

print(p1)
print(p2)
