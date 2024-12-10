lines = enumerate(open("../input/d10.txt").readlines())
                  
G = {
    (x, y): int(height)
    for y, line in lines
    for x, height in enumerate(line.strip())
}

DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def print_path(path):
    
    for y, line in lines:
        ln = []
        for x, height in enumerate(line.strip()):
            if (x, y) in path:
                ln.append(f"\033[1;31m{height}\033[0m")
            else:
                ln.append(height)

        print("".join(ln))
    
    print()


def find_path(pos, height, seen=set(), path=[]):
    if pos in seen:
        return []

    value = G.get(pos)
    if value is None or value != height:
        return []

    seen.add(pos)
    path.append(pos)

    paths = []
    if value == 9:
        paths.append(path[:])
    else:
        for dx, dy in DIR:
            paths.extend(find_path((pos[0] + dx, pos[1] + dy), height + 1, seen, path))

    seen.remove(pos)
    path.pop()

    return paths

p1 = 0
p2 = 0
for pos, height in G.items():
    if height == 0:
        paths = find_path(pos, height)        
        distinct_paths = set()
        for p in paths:
            distinct_paths.add(p[-1])
        p1 += len(distinct_paths)    
        p2 += len(paths)

print(p1)        
print(p2)