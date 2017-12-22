with open('../resources/day19.input') as f:
    lines = [l for l in f]

orientation = 'down'
chars = []
orients = {'left': (0, -1), 'up': (-1, 0), 'right': (0, 1), 'down': (1, 0)}
finished = False



def find_start(lines):
    idx = 0
    for char in lines[0]:
        if char == '|':
            return idx
        idx += 1

def get_char_at(y, x):
    try:
        return lines[y][x]
    except IndexError:
        return ' '

def handle_branch(y, x):
    global orientation

    if orientation in ('left', 'right'):
        dy, dx = orients['up']
        y_dy = y + dy
        x_dx = x + dx

        if not get_char_at(y_dy, x_dx).isspace():
            orientation = 'up'
            return y_dy, x_dx
        else:
            dy, dx = orients['down']
            orientation = 'down'
            return y + dy, x + dx
    else:
        dy, dx = orients['left']
        y_dy = y + dy
        x_dx = x + dx
        if not get_char_at(y_dy, x_dx).isspace():
            orientation = 'left'
            return y_dy, x_dx
        else:
            dy, dx = orients['right']
            orientation = 'right'
            return y + dy, x + dx


def get_next(y, x):
    global finished
    char = lines[y][x]
    if char == ' ':
        finished = True
        return y, x
    if char == '+':
        return handle_branch(y, x)
    if ord(char) in range(65, 123):
        chars.append(char)

    return y + orients[orientation][0], x + orients[orientation][1]


x = find_start(lines)
y = 0
cnt = 0
while not finished:
    y, x = get_next(y, x)
    cnt += 1

print(''.join(chars))
print(cnt - 1)
