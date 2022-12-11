from collections import defaultdict
import copy
from enum import Enum
from functools import reduce
from itertools import groupby
import operator


class Op(Enum):
    ADD = 1,
    MUL = 2,
    ADD_SELF = 3,
    MUL_SELF = 4


class Monkey:
    def __init__(self, num, items: list[str], op, oprd, divisor, targets):
        self.num = num
        self.counter = 0
        self.divisor = divisor
        self.items = items
        match op:
            case Op.MUL:
                def mul(a, supermod):
                    if supermod:
                        return (a % supermod) * oprd
                    else:
                        return (a * oprd) // 3
                self.op = mul
            case Op.MUL_SELF:
                def selfmul(a, supermod):
                    if supermod:
                        return (a % supermod) * a
                    else:
                        return (a * a) // 3
                self.op = selfmul
            case Op.ADD:
                def add(a, supermod):
                    if supermod:
                        return (a % supermod) + oprd
                    else:
                        return (a + oprd) // 3
                self.op = add
            case Op.ADD_SELF:
                def selfadd(a, supermod):
                    if supermod:
                        return (a % supermod) + (a % supermod)
                    else:
                        return (a + a) // 3
                self.op = selfadd

        self.action = lambda a: (
            targets[0], a) if a % divisor == 0 else (targets[1], a)

    def run(self, supermod):
        self.items = [self.op(item, supermod) for item in self.items]
        targets = [self.action(item) for item in self.items]
        self.counter += len(self.items)
        self.items = []
        res = defaultdict(list)
        for (k, g) in targets:
            res[k].append(g)
        return res

    def __repr__(self) -> str:
        return f'Monkey {self.num} inspected {self.counter} times and has items: {self.items}\n'


def parse_monkey(input: list[str]):
    num = int(input[0][-2:-1])
    items = [int(item) for item in input[1].split(':')[1].strip().split(',')]
    operands = input[2].split('=')[1].strip().split(' ')
    oprd = None if operands[2] == 'old' else int(operands[2])
    match operands[1]:
        case '*':
            op = Op.MUL if oprd else Op.MUL_SELF
        case '+':
            op = Op.ADD if oprd else Op.ADD_SELF
        case _:
            raise Exception("unknown op")
    divisor = int(input[3].split(' ').pop())
    target_t = int(input[4].split(' ').pop())
    target_f = int(input[5].split(' ').pop())

    return Monkey(num, items, op, oprd, divisor, (target_t, target_f))


def simulate(monkeys, rounds, supermod=None):
    for i in range(rounds):
        for i in range(len(monkeys)):
            res = monkeys[i].run(supermod)
            for m, items in res.items():
                monkeys[m].items.extend(items)
    toplist = sorted(monkeys, key=lambda m: m.counter, reverse=True)
    return toplist[0].counter * toplist[1].counter



monkeys = [parse_monkey(m.split("\n"))
           for m in open("input/11").read().split("\n\n")]

supermod = reduce(operator.mul, map(lambda m: m.divisor, monkeys), 1)

m2 = copy.deepcopy(monkeys)

p1 = simulate(monkeys, 20)
p2 = simulate(m2, 10000, supermod)

print(p1)
print(p2)