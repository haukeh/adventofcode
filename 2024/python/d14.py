from dataclasses import dataclass
from typing import Tuple


@dataclass
class Robot:
    p: Tuple[int]
    v: Tuple[int]


HSIZE = 101
VSIZE = 103
HMID = HSIZE // 2
VMID = VSIZE // 2


def print_grid(robots):
    rs = {r.p for r in robots}
    for y in range(VSIZE):
        ln = []
        for x in range(HSIZE):
            if (x, y) in rs:
                ln.append("#")
            else:
                ln.append(".")

        print("".join(ln))
    print()


robots = []


def simulate(secs):
    for _ in range(secs):
        for r in robots:
            x, y = r.p
            dx, dy = r.v
            xx = (x + dx) % HSIZE
            yy = (y + dy) % VSIZE
            r.p = (xx, yy)


def p1(robots):
    tl, tr, br, bl = (0, 0, 0, 0)
    for r in robots:
        x, y = r.p

        if x != HSIZE // 2 and y != VSIZE // 2:
            if x < HMID and y < VMID:
                tl += 1
            elif x > HMID and y < VMID:
                tr += 1
            elif x > HMID and y > VMID:
                br += 1
            elif x < HMID and y > VMID:
                bl += 1

    return tl * tr * br * bl


lines = [line.strip().split() for line in open("../input/d14.txt").readlines()]

robots = []
for a, b in lines:
    _, pp = a.split("=")
    _, vv = b.split("=")
    p = tuple(map(int, pp.split(",")))
    v = tuple(map(int, vv.split(",")))
    robots.append(Robot(p, v))

CC = {(HMID, i) for i in range(VSIZE)}

i = 0
while True:
    rpos = set()
    for r in robots:
        x, y = r.p
        dx, dy = r.v
        xx = (x + dx) % HSIZE
        yy = (y + dy) % VSIZE
        new_pos = (xx, yy)
        r.p = new_pos
        rpos.add(new_pos)    
    
    i += 1

    if i == 100:
        print(p1(robots))
    

    sec = CC.intersection(rpos)

    if len(sec) >= 20:
        print(f"=== {i} ===")
        print_grid(robots)