elves = [sum(x) for x in [[int(l) for l in g.split('\n')] for g in open("input/01").read().split("\n\n")]]
print('p1: {}'.format(max(elves)))
print('p2: {}'.format(sum(sorted(elves, reverse=True)[:3])))