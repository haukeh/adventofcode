grid, instructions = open("../input/d15.txt").read().split("\n\n")

instructions = instructions.replace("\n", "")

G = {(x, y): c for y, line in enumerate(grid.split("\n")) for x, c in enumerate(line)}

start = next(pos for pos, item in G.items() if item == "@")


def print_grid():
    rows = grid.split("\n")
    for y in range(len(rows)):
        line = []
        for x in range(len(rows[0])):
            line.append(G[(x, y)])
        print("".join(line))


def get_dir(inst):
    match inst:
        case "^":
            return (0, -1)
        case ">":
            return (1, 0)
        case "v":
            return (0, 1)
        case "<":
            return (-1, 0)


pos = start
for i in instructions:
    dx, dy = get_dir(i)
    next = (pos[0] + dx, pos[1] + dy)
    match G.get(next):
        case "#":
            continue
        case ".":
            G[pos] = "."
            G[next] = "@"
            pos = next
        case "O":
            shift = 1
            after = (next[0] + dx, next[1] + dy)
            av = G.get(after)
            while av == "O":
                shift += 1
                after = (after[0] + dx, after[1] + dy)
                av = G.get(after)
            match av:
                case "#":
                    continue
                case ".":
                    while shift > 0:
                        G[after] = "O"
                        x, y = after                        
                        after = (x - dx, y - dy)
                        shift -= 1
                    
                    G[after] = "@"
                    G[pos] = "."
                    pos = next                    
    # print(f"Move {i}:")
    # print_grid()

p1 = 0

for x, y in [pos for pos, v in G.items() if v == "O"]:
    p1 += 100 * y + x

print(p1)
