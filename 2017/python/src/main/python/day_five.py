def jumper(func):
    with open("../resources/day5.input") as f:
        jumps = [int(line.rstrip()) for line in f]
    next_pos = 0
    jump_counter = 0
    while 0 <= next_pos <= len(jumps) - 1:
        current_pos = next_pos
        offset = jumps[current_pos]
        jumps[current_pos] = func(jumps[current_pos])
        next_pos += offset
        jump_counter += 1
    return jump_counter


print(jumper(lambda entry: (entry + 1)))

print(jumper(lambda entry: (entry + 1 if entry < 3 else entry - 1)))
