def explode(string):
    return [list(row) for row in string.split('/')]


def flatten_rule(matrix):
    return '/'.join(''.join(row) for row in matrix)


def rotate_right(m):
    return list(map(list, zip(*m[::-1])))


def flip_horizontal(m):
    return [row[::-1] for row in m]


def flip_vertical(m):
    return m[::-1]


rules = {}

with open('../resources/day21.input') as f:
    for line in f:
        before, after = line.split(' => ')
        input = explode(before.strip())
        output = explode(after.strip())

        rotation = input
        for _ in range(4):
            rotation = rotate_right(rotation)
            rules[flatten_rule(rotation)] = output
        rotation = flip_vertical(rotation)
        for _ in range(4):
            rotation = rotate_right(rotation)
            rules[flatten_rule(rotation)] = output


def split(mat, step):
    new = []
    for i in range(len(mat) // step * (step + 1)):
        new.append([])

    for y in range(0, len(mat), step):
        for x in range(0, len(mat), step):
            res = []
            for i in range(0, step):
                res.append(mat[y + i][x:step + x])

            part = rules[flatten_rule(res)]

            for z, row in enumerate(part):
                idx = y // step * (step + 1) + z
                new[idx] += row

    return new


current = explode('.#./..#/###')

for i in range(18):
    step = 2 if len(current) % 2 == 0 else 3
    current = split(current, step)

count = 0

for row in current:
    for c in row:
        if c == '#':
            count += 1

print(count)
