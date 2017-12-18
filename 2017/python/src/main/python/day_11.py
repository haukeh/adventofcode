with open('../resources/day11.input') as f:
    steps = f.read().strip().split(',')

    x = 0
    y = 0
    z = 0

    distances = []

    for step in steps:
        if step == 'n':
            y += 1
            z -= 1
        elif step == 'ne':
            x += 1
            z -= 1
        elif step == 'se':
            y -= 1
            x += 1
        elif step == 's':
            y -= 1
            z += 1
        elif step == 'sw':
            x -= 1
            z += 1
        elif step == 'nw':
            y += 1
            x -= 1
        distances.append((abs(x) + abs(y) + abs(z)) / 2)

    print((abs(x) + abs(y) + abs(z)) / 2)
    print(max(distances))
