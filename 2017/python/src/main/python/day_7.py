with open('../resources/day7.input') as f:
    progs = []
    has_parent = set()
    for line in f:
        line = line.strip().split()
        progs.append(line[0])
        if '->' in line:
            idx = line.index('->')
            children = [c.strip(',') for c in line[idx + 1:]]
            for child in children:
                has_parent.add(child)

    for prog in progs:
        if prog not in has_parent:
            print(prog)
