from collections import defaultdict


def is_number(str):
    return not 'a' <= str <= 'z'


def get_val(val, reg):
    if not 'a' <= val <= 'z':
        return int(val)
    else:
        return reg[val]


def setfunc(x, y):
    def func(reg):
        reg[x] = get_val(y, reg)

    return func


def addfunc(x, y):
    def func(reg):
        reg[x] += get_val(y, reg)

    return func


def mulfunc(x, y):
    def func(reg):
        reg[x] *= get_val(y, reg)

    return func


def modfunc(x, y):
    def func(reg):
        reg[x] %= get_val(y, reg)

    return func


def subfunc(x, y):
    def func(reg):
        reg[x] -= get_val(y, reg)

    return func


def rcvfunc(x, y):
    def func(reg, queue):
        if reg[x] > 0:
            return queue[0]

    return func


def sndfunc(x, y):
    def func(reg, queue):
        queue.appendleft(reg[x])

    return func


funcs = {'set': setfunc, 'add': addfunc, 'mul': mulfunc, 'mod': modfunc,
         'sub': subfunc}

registers = defaultdict(int)

with open('in/day23.input') as f:
    lines = [line.split() for line in f]

i = 0
muls = 0
loops = 0
while 0 <= i < len(lines):
    loops += 1
    print(i)

    op, p1, p2 = lines[i]

    if op == 'jnz':
        if get_val(p1, registers) != 0:
            i += get_val(p2, registers)
        else:
            i += 1
    else:
        funcs[op](p1, p2)(registers)
        if op == 'mul':
            muls += 1
        i += 1

    print(muls)

b = 99 * 100 + 100000
c = b + 17000
h = 0


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True


for i in range(1001):

    if not is_prime(b):
        h += 1

    b += 17

print(h)
