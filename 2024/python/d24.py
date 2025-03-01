from collections import deque

init, rules = open("../input/d24.txt").read().split("\n\n")

R = {}

for x in init.split("\n"):
    pos, val = x.split(":")
    R[pos.strip()] = int(val.strip())


def mkfunc(a, b, op, c):
    def func():
        aa = R.get(a)
        bb = R.get(b)

        if aa is not None and bb is not None:
            match op.strip():
                case "AND":
                    res = aa & bb
                case "OR":
                    res = aa | bb
                case "XOR":
                    res = aa ^ bb

            R[c] = res

            return res

        return None

    return func


fns = deque()
for r in rules.split("\n"):
    f, target = r.split(" -> ")
    a, op, b = f.split()
    fns.append(mkfunc(a, b, op, target))

while len(fns) > 0:
    next = fns.popleft()
    res = next()
    if res is None:
        fns.append(next)

zs = [
    value
    for _, value in sorted(
        [(item, value) for (item, value) in R.items() if item.startswith("z")],
        reverse=True,
    )
]

p1 = int("".join(map(str, zs)), 2)

print(p1)
