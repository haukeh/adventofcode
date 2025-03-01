import itertools


keys = []
locks = []


def parse(item):
    res = []
    if all(i == "#" for i in item[0]) and all(i == "." for i in item[-1]):
        for x in range(len(item[0])):
            res.append(
                len(
                    list(
                        filter(
                            lambda x: x == "#",
                            [item[y][x] for y in range(1, len(item))],
                        )
                    )
                )
            )

        locks.append(res)

    elif all(i == "." for i in item[0]) and all(i == "#" for i in item[-1]):
        for x in range(len(item[0])):
            res.append(
                len(
                    list(
                        filter(
                            lambda x: x == "#",
                            [item[y][x] for y in range(len(item) - 2, 0, -1)],
                        )
                    )
                )
            )

        keys.append(res)


[parse(block.split("\n")) for block in open("../input/d25.txt").read().split("\n\n")]

LIM = 6

fit = 0
for lock in locks:
    for key in keys:
        if all(a + b < LIM for a, b in zip(lock, key)):
            fit += 1

print(fit)
