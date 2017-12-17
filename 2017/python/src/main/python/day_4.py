from itertools import combinations

with open("../resources/day4.input") as f:
    lines = [line.split() for line in f]


def get_valid_p1():
    valid = 0
    sets = [set(line) for line in lines]
    for i in range(len(lines)):
        if len(lines[i]) == len(sets[i]):
            valid += 1
    return valid


def get_valid_p2():
    valid = 0
    for line in lines:
        if all(not is_anagram(s1, s2) for s1, s2 in combinations(line, 2)):
            valid += 1
    return valid


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    freqs1 = {}
    freqs2 = {}
    for c in s1:
        if c in freqs1:
            freqs1[c] += 1
        else:
            freqs1[c] = 1

    for c in s2:
        if c in freqs2:
            freqs2[c] += 1
        else:
            freqs2[c] = 1

    return True if freqs1 == freqs2 else False


print(get_valid_p1())
print(get_valid_p2())
