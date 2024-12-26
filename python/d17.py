import copy


DEBUG = False

reg, ins = open("../input/d17.txt").read().split("\n\n")

A, B, C = list(map(int, [ln.split(":")[1].strip() for ln in reg.split("\n")]))
instructions = list(map(lambda i: int(i.strip()), ins.split(":")[1].split(",")))
ip = 0


def run(a, b, c, ins):
    A, B, C = (a, b, c)
    instructions = ins
    ip = 0
    out = []

    def get_cmb_op(op):
        match op:
            case 0 | 1 | 2 | 3 as x:
                return x
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C
            case x:
                raise Exception(f"combo operand {x} is invalid")

    def div(op, numerator):
        cmb = get_cmb_op(op)
        if DEBUG:
            print(f"A = {numerator} // (2**{cmb}) = {numerator // (2**cmb)}")

        return numerator // (2**cmb)

    while True:
        if ip > len(instructions) - 2:
            break

        opcode, op = instructions[ip : ip + 2]

        match opcode:
            # adv
            case 0:
                A = div(op, A)
            # bxl
            case 1:
                B = B ^ op
            # bst
            case 2:
                B = get_cmb_op(op) % 8
            # jnz
            case 3:
                if A != 0:
                    ip = op
                    continue
            # bxc
            case 4:
                B = B ^ C
            # out
            case 5:
                out.append(get_cmb_op(op) % 8)
            # bdv
            case 6:
                B = div(op, A)
            # cdv
            case 7:
                C = div(op, A)

        ip += 2

    return out


# A = 6624566500
res = []

p1 = run(A, B, C, instructions)

print(",".join(map(str, p1)))

n = 8**8
res = []
print(instructions)
i = 0
while i < 1000:
    res = run(n, B, C, instructions)    
    print(f"A={n}: {res}")
    n += 1
    i += 1
    