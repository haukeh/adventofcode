import copy
import math
from collections import defaultdict
from enum import Enum


class Op(Enum):
    ADD = 1,
    MUL = 2,
    ADD_SELF = 3,
    MUL_SELF = 4


class Monkey:
    def __init__(self, num, items, op, divisor, true, false):
        self.num = num
        self.counter = 0
        self.divisor = divisor
        self.items = items
        self.op = lambda old: eval(op)
        self.true = true
        self.false = false

    def run(self, lcm, p1=False):
        res = defaultdict(list)
        for item in self.items:
            item = item % lcm if not p1 else item
            opres = self.op(item)
            if p1:
                opres //= 3
            target = self.true if opres % self.divisor == 0 else self.false
            res[target].append(opres)
        self.counter += len(self.items)
        self.items = []
        return res

    def __repr__(self) -> str:
        return f'Monkey {self.num} inspected {self.counter} times and has items: {self.items}\n'


def parse_monkey(input: list[str]):
    num = int(input[0][-2:-1])
    items = [int(item) for item in input[1].split(':')[1].strip().split(',')]
    op = input[2].split('=')[1]
    divisor = int(input[3].split(' ').pop())
    target_t = int(input[4].split(' ').pop())
    target_f = int(input[5].split(' ').pop())

    return Monkey(num, items, op, divisor, target_t, target_f)


def simulate(monkeys, rounds, lcm=None, p1=False):
    for i in range(rounds):
        for i in range(len(monkeys)):
            res = monkeys[i].run(lcm, p1)
            for m, items in res.items():
                monkeys[m].items.extend(items)
    toplist = sorted(monkeys, key=lambda m: m.counter, reverse=True)
    return toplist[0].counter * toplist[1].counter


monkeys = [parse_monkey(m.split("\n"))
           for m in open("input/11").read().split("\n\n")]

lcm = math.lcm(*map(lambda m: m.divisor, monkeys))

m2 = copy.deepcopy(monkeys)

p1 = simulate(monkeys, 20, lcm, p1=True)
p2 = simulate(m2, 10000, lcm)

print(p1)
print(p2)
