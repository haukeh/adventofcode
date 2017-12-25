# print(sum(map(lambda x: x[0] + x[1], starters)))


def search(bridge, port, cmps):
    left = [comp for comp in cmps if port in comp]

    if len(left) == 0:
        return [bridge]

    bridges = []

    for l in left:
        nxt = l[0] if l[0] != port else l[1]
        c = cmps[:]
        c.remove(l)
        bridges += search(bridge + [l], nxt, c)

    return bridges


with open('in/day24.input') as f:
    comps = [tuple(map(int, line.strip().split('/'))) for line in f]

res = search([], 0, comps)

# sums = [sum(map(lambda x: x[0] + x[1], r)) for r in res]
#
# longest = sorted(res, key=lambda x: len(x), reverse=True)

lenandsum = sorted(
    list(map(lambda x: (len(x), sum(map(lambda x: x[0] + x[1], x))), res)),
    key=lambda x: x[0], reverse=True)

print(lenandsum[:20])
