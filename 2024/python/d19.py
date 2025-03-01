import functools


a, b = open("../input/d19.txt").read().split("\n\n")
patterns = sorted(list(map(lambda s: s.strip(), a.split(","))), key=len, reverse=True)

designs = b.split("\n")


@functools.cache
def possible(design):
    if design == "":
        return True

    for pat in patterns:
        if design.startswith(pat) and possible(design[len(pat) :]):
            return True

    return False


@functools.cache
def possibilities(design):
    if design == "":
        return 1

    ans = 0
    for pat in patterns:
        if design.startswith(pat):
            ans += possibilities(design[len(pat) :])

    return ans


p1 = 0
p2 = 0
for design in designs:
    if possible(design):
        p1 += 1
    
    p2 += possibilities(design)

print(p1)
print(p2)
