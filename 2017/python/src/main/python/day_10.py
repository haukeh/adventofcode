from functools import reduce

with open('../resources/day10.input') as f:
    lens = [ord(c) for c in f.read()]
    lens.extend([17, 31, 73, 47, 23])
    lst_len = 256
    lst = [num for num in range(0, lst_len)]
    pos = 0
    skip = 0
    for i in range(0, 64):
        for length in lens:
            sublist = [lst[i % lst_len] for i in range(pos, pos + length)][::-1]
            for i in range(0, length):
                lst[(pos + i) % lst_len] = sublist[i]
            pos = pos + length + skip
            skip += 1

    splits = [lst[i:i + 16] for i in range(0, len(lst), 16)]

    hashes = [reduce(lambda x, y: x ^ y, split) for split in splits]

    out = ""
    for hash in hashes:
        out += '{:02x}'.format(hash)

    print(out)
