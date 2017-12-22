progs = [chr(c) for c in range(ord('a'), ord('p') + 1)]

with open('../resources/day16.input') as f:
    moves = [move for move in f.read().split(',')]


def spin(progs, steps):
    return progs[-steps:] + progs[:len(progs) - steps]


def exchange(progs, idx1, idx2):
    a = progs[idx1]
    b = progs[idx2]
    progs[idx1] = b
    progs[idx2] = a
    return progs


def partner(progs, p1, p2):
    idx1 = progs.index(p1)
    idx2 = progs.index(p2)
    progs[idx1] = p2
    progs[idx2] = p1
    return progs


seen = []
for i in range(0, 1000000000):

    if "".join(progs) in seen:
        print(seen[1000000000 % i])
        break
    seen.append("".join(progs))

    for move in moves:
        if move.startswith('s'):
            progs = spin(progs, int(move[1:]))
        elif move.startswith('x'):
            parts = move.split('/')
            idx1 = int(parts[0][1:])
            idx2 = int(parts[1])
            progs = exchange(progs, int(idx1), int(idx2))
        elif move.startswith('p'):
            parts = move.split('/')
            p1 = parts[0][1:]
            p2 = parts[1]
            progs = partner(progs, p1, p2)

print("".join(progs))
