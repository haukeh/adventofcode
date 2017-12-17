with open('../resources/day13.input') as f:
    lines = [line.strip().split(':') for line in f]
    mapping = {int(pair[0]): int(pair[1]) for pair in lines}


    def scanpos(pos, depth):
        return pos % (2 * (depth - 1))


    severity = 0
    for i in mapping.keys():
        if scanpos(i, mapping[i]) == 0:
            severity += i * mapping[i]

    print(severity)

    delay = 0
    caught = True
    while caught:
        caught = False
        for i in mapping.keys():
            if scanpos(i + delay, mapping[i]) == 0:
                caught = True
                delay += 1
                break

    print(delay)
