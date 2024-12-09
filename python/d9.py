import itertools


def dbg_print(disk):
    print("".join(map(lambda s: "." if s == "-1" else s, map(str, disk))))


nums = list(map(int, open("../input/d9.txt").read()))
if len(nums) // 2 != 0:
    nums = nums + [0]


def p1():
    disk = []
    for id, (fsize, space) in enumerate(zip(nums[::2], nums[1::2])):
        disk = disk + [id] * fsize + space * [-1]

    i = disk.index(-1)
    j = len(disk) - 1

    print(len(disk))

    while i <= j:
        tmp = disk[j]
        disk[j] = disk[i]
        disk[i] = tmp

        while disk[i] != -1:
            i += 1
        while disk[j] == -1:
            j -= 1

    chksum = sum(
        [i * n for i, n in enumerate(itertools.takewhile(lambda n: n != -1, disk))]
    )

    return chksum


def p2():
    disk = []
    for id, (fsize, space) in enumerate(zip(nums[::2], nums[1::2])):
        disk = disk + [id] * fsize + space * [-1]

    i = disk.index(-1)
    j = len(disk) - 1
    dbg_print(disk)

    while i <= j:
        file_end = j
        elem = disk[j]
        # while elem == -1:
        #     j -= 1
        while disk[j] == elem:
            j -= 1
        file_start = j + 1
        file_len = file_end - file_start + 1

        while i < j:
            start_free = i
            elem = disk[i]
            while disk[i] == -1:
                i += 1
            free_len = i - start_free
            if free_len >= file_len:
                file = disk[file_start : file_end + 1]
                disk[start_free : start_free + file_len]
                disk[start_free : start_free + file_len] = file
                disk[file_start : file_end + 1] = [-1] * file_len
                break
            else:
                i = disk.index(-1, i)
            
        i = disk.index(-1)

    chksum = 0
    for i, n in enumerate(disk): 
        if n != -1: 
            chksum += i * n

    return chksum


# print(p1())
print(p2())
