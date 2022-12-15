import re 

pat = r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'

def parse(line): 
    m = re.match(pat, line)
    return ((int(m.group(1)), int(m.group(2))),(int(m.group(3)), int(m.group(4))))

items = [parse(line) for line in open("input/15_t").read().split('\n')]

G = {}

def taxicab(a, b): 
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for (sensor, beacon) in items: 
    G[sensor] = 'S'
    G[beacon] = 'B'

for (sensor, beacon) in items: 
    distance = taxicab(sensor, beacon)
    print(f'{sensor} and {beacon} have distane {distance}')
    for dir in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        for i in range(0, distance+1):
            for j in range(0, distance + 1):
                aa = (sensor[0] + i * dir[0], sensor[1] + j * dir[1])
                if taxicab(aa, sensor) <= distance: 
                    if not aa in G:
                        G[aa] = "#"
    

count = 0
for ((x,y), v) in G.items():
    if y == 10 and v == '#':
        count += 1
print(count)

def print():
    for y in range(-2, 23):
        r = []
        for x in range(-2, 26):
            if (x, y) in G: 
                r.append(G[(x, y)])
            else:
                r.append('.')
        print(''.join(r))
