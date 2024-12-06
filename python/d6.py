lines = [list(line.strip()) for line in open("../input/d6.txt").readlines()]
grid = {(x, y): c for y, xs in enumerate(lines) for x, c in enumerate(xs)}
start = [key for key, value in grid.items() if value == "^"][0]


def p1():
    visited = set()
    pos = start
    dir = (0, -1)
    while pos in grid:
        visited.add(pos)
        next = (pos[0] + dir[0], pos[1] + dir[1])
        if not next:
            break

        item = grid.get(next)
        if item == "#":
            dx, dy = dir
            dir = (-dy, dx)

        pos = (pos[0] + dir[0], pos[1] + dir[1])

    print(len(visited))


def p2():
    loops = 0    

    for obs, v in grid.items():
        visited = set()        
        pos = start                
        dir = (0, -1)
        if v == ".":                        
            while pos in grid:
                if (pos, dir) in visited:                    
                    loops += 1
                    break

                visited.add((pos, dir))

                next = (pos[0] + dir[0], pos[1] + dir[1])                
                item = grid.get(next)
                if item is None:                    
                    break
                
                if item == "#" or next == obs:
                    dx, dy = dir
                    dir = (-dy, dx)                
                else:
                    pos = next
        else:
            continue
        
    print(loops)


p1()
p2()
