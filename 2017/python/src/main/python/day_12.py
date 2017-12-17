from collections import defaultdict

with open('../resources/day12.input') as f:
    conns = defaultdict(set)
    for line in f:
        left, right = line.strip().split('<->')
        leftnum = int(left)
        rightnums = [int(num) for num in right.strip().split(',')]
        conns[leftnum].update(rightnums)
        for num in rightnums:
            conns[num].add(leftnum)


def graph_of(num):
    found = {num}
    left = [num]
    while left:
        new = conns[left.pop()]
        for i in new:
            if i not in found:
                left.append(i)
        found.update(new)
    return found


print(len(graph_of(0)))

nums = set(conns)

groups = 0
while nums:
    groups += 1
    group = graph_of(nums.pop())
    nums = nums - group

print(groups)
