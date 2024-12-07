import functools
import itertools
from operator import add, mul


def concat(a: int, b: int):
    return int(f"{str(a)}{str(b)}")


OPS = [add, mul, concat]


def parse(line):
    result, opline = line.split(":")
    operands = [int(op) for op in opline.strip().split(" ")]
    return int(result.strip()), operands


equations = [parse(line) for line in open("../input/d7.txt").readlines()]


def solve(p2: bool):
    solvable = []
    operators = OPS if p2 else OPS[:2]

    for wanted, operands in equations:
        permutations = itertools.product(operators, repeat=len(operands))

        for ops in permutations:
            oplist = list(ops)

            def reduce_func(operations, a, b):
                op = operations.pop(0)
                return op(a, b)

            res = functools.reduce(functools.partial(reduce_func, oplist), operands, 0)

            if res == wanted:
                solvable.append(wanted)
                break

    return solvable


p1 = sum(solve(p2=False))
p2 = sum(solve(p2=True))

print(p1)
print(p2)
