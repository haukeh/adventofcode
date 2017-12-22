from collections import defaultdict

grid = defaultdict(lambda: '.')

with open('../resources/day22.input') as f:
    lines = f.read().splitlines()

for y, line in enumerate(lines):
    for x, col in enumerate(line):
        grid[(y, x)] = col

dirs = ['l', 'u', 'r', 'd']

transitions = {'.': 'W', 'W': '#', '#': 'F', 'F': '.'}

x = len(lines) // 2
y = x
direction = 'u'

infections = 0

for _ in range(10000000):
    node = grid[(y, x)]

    if node == '.':
        direction = dirs[(dirs.index(direction) - 1) % 4]
    elif node == '#':
        direction = dirs[(dirs.index(direction) + 1) % 4]
    elif node == 'F':
        direction = direction = dirs[(dirs.index(direction) + 2) % 4]

    new_state = transitions[node]
    if new_state == '#':
        infections += 1
    grid[(y, x)] = new_state

    if direction == 'u':
        nxt = x, y - 1
    elif direction == 'r':
        nxt = x + 1, y
    elif direction == 'd':
        nxt = x, y + 1
    else:
        nxt = x - 1, y

    x, y = nxt

print(infections)
