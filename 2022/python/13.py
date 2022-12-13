from functools import cmp_to_key
import itertools


def compare(a, b): 
    # print(f"comparing {a} and {b}")
    if isinstance(a, list) and isinstance(b, list):
        if a == b:
            return 0
        if len(b) == 0: 
            return 1
        if len(a) == 0:
            return -1

        return compare(a[0], b[0]) or compare(a[1:], b[1:])

    if isinstance(a, int) and isinstance(b, int):      
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1          
    
    if isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    
    if isinstance(a, int) and isinstance(b, list):
        return compare([a], b)

    assert(False)
        


p1 = []
for raw_pairs in open('input/13').read().split('\n\n'):
    p1.append(list(map(eval, raw_pairs.split('\n'))))

already_sorted = []
for i, x in enumerate(p1):
    if compare(x[0], x[1]) == -1:
        already_sorted.append(i + 1)

p1 = sum(already_sorted)

print(p1)

p2 = [eval(line) for line in open('input/13').read().replace('\n\n', '\n').split('\n')]
p2.extend([[[6]], [[2]]])
p2 = sorted(p2, key=cmp_to_key(compare))

print((p2.index([[2]]) + 1) * (p2.index([[6]]) + 1))