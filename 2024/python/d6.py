def sim_guard(grid, start):
    visited = set()
    pos = start
    dir = (0, -1)
    loop = False

    while pos in grid:
        if (pos, dir) in visited:
            loop = True
            break

        visited.add((pos, dir))
        
        next = (pos[0] + dir[0], pos[1] + dir[1])
        item = grid.get(next)
        if item is None:
            break

        if item == "#":
            dx, dy = dir
            dir = (-dy, dx)
        else:
            pos = next

    return set(map(lambda p: p[0], visited)), loop


grid = {
    (x, y): char
    for y, line in enumerate(open("../input/d6.txt").readlines())
    for x, char in enumerate(line.strip())
}

start = next(key for key, value in grid.items() if value == "^")
guard_path, _ = sim_guard(grid, start)

p1 = len(guard_path)
p2 = 0
for pos in guard_path:
    if grid[pos] == ".":
        grid[pos] = "#"

        _, loop = sim_guard(grid, start)

        if loop:
            p2 += 1

        grid[pos] = "."


print(p1)
print(p2)
