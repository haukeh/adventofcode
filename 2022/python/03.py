from functools import reduce

lines = [l for l in open('input/03').read().strip().split('\n')]


def prio(rucksacks):
    c = reduce(lambda a, b: a & b, [set(r) for r in rucksacks]).pop()
    return ord(c) - ord('a') + 1 if c.islower() else ord(c) - ord('A') + 27

p1 = sum([prio([l[:len(l) // 2], l[len(l) // 2:]]) for l in lines])
p2 = sum([prio(lines[i:i+3]) for i in range(0, len(lines), 3)])

print(p1)
print(p2)
