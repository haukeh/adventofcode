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
        reg[x] = int(y) if is_number(y) else reg[y]

    return func


def addfunc(x, y):
    def func(reg):
        reg[x] += int(y) if is_number(y) else reg[y]

    return func


def mulfunc(x, y):
    def func(reg):
        reg[x] *= int(y) if is_number(y) else reg[y]

    return func


def modfunc(x, y):
    def func(reg):
        reg[x] %= int(y) if is_number(y) else reg[y]

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


funcs = {'set': setfunc, 'add': addfunc, 'mul': mulfunc, 'mod': modfunc}


def run(pid, registers, myqueue, otherqueue):
    global states, one_sends, idx

    while 0 <= idx[pid] < len(lines) and states[pid] != 'F':
        # print(registers)
        i = idx[pid]
        op, p1, p2 = lines[i] if len(lines[i]) == 3 else lines[i] + [None]

        if op == 'rcv':
            if len(myqueue) == 0:
                states[pid] = 'W'
                break
            else:
                registers[p1] = myqueue.pop(0)
        elif op == 'snd':
            if pid == 1:
                one_sends += 1
            otherqueue.append(get_val(p1, registers))
        elif op == 'jgz':
            if get_val(p1, registers) > 0:
                idx[pid] += get_val(p2, registers)
            else:
                idx[pid] += 1
        else:
            funcs[op](p1, p2)(registers)

        if op != 'jgz':
            idx[pid] += 1

    if states[pid] != 'W':
        states[pid] = 'F'


with open('../resources/day18.input') as f:
    lines = [line.split() for line in f]

reg_0 = defaultdict(lambda: 0)
reg_0['p'] = 0

reg_1 = defaultdict(lambda: 0)
reg_1['p'] = 1

q0 = []
q1 = []

idx = [0, 0]

states = ['R', 'R']

one_sends = 0

while 'R' in states or len(q1) > 0 or len(q0) > 0:
    run(0, reg_0, q0, q1)
    run(1, reg_1, q1, q0)

print(one_sends)
