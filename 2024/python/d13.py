import re
from dataclasses import dataclass


@dataclass
class ClawMachine:
    ax: int
    ay: int
    bx: int
    by: int
    px: int
    py: int


BUTTON_PATTERN = r".*X([+-]\d+)\, Y([+-]\d+)"
PRIZE_PATTERN = r".*X=(\d+)\, Y=(\d+)"


def parse_machine(input):
    aa, bb, pp = input.split("\n")
    ma = re.match(BUTTON_PATTERN, aa)
    mb = re.match(BUTTON_PATTERN, bb)
    mp = re.match(PRIZE_PATTERN, pp)
    ax = int(ma.group(1))
    ay = int(ma.group(2))
    bx = int(mb.group(1))
    by = int(mb.group(2))
    px = int(mp.group(1))
    py = int(mp.group(2))
    return ClawMachine(ax, ay, bx, by, px, py)


machines = [parse_machine(m) for m in open("../input/d13.txt").read().split("\n\n")]


# TIL: Cramer's rule
# https://www.reddit.com/r/adventofcode/comments/1hd7irq/2024_day_13_an_explanation_of_the_mathematics/
# https://www.youtube.com/watch?v=jBsC34PxzoM
def solve_cramer(m, p2=False):
    res = 0

    if p2:
        m.px = m.px + 10000000000000
        m.py = m.py + 10000000000000

    det = m.ax * m.by - m.ay * m.bx
    A = (m.px * m.by - m.py * m.bx) // det
    B = (m.ax * m.py - m.ay * m.px) // det

    if (m.ax * A + m.bx * B == m.px) and (m.ay * A + m.by * B == m.py):
        res = 3 * A + B

    return res


p1 = 0
p2 = 0

for m in machines:
    p1 += solve_cramer(m)
    p2 += solve_cramer(m, True)

print(p1)
print(p2)
