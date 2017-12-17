def part_one():
    buf = [0]
    steps = 370
    curr = 0
    for i in range(1, 2017):
        idx = (curr + steps) % len(buf)
        buf = buf[:idx + 1] + [i] + buf[idx + 1:]
        print(buf[1])
        curr = idx + 1


def part_2():
    steps = 370
    length = 1
    curr = 0
    for i in range(1, 50000000):
        idx = (curr + steps) % length
        if idx == 0:
            print(i)
        curr = idx + 1
        length += 1
