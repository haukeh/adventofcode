import re

pat = r'(-?\d+)'


def parse(line):
    sx, sy, bx, by = re.findall(pat, line)
    return [(int(sx), int(sy)), (int(bx), int(by))]


items = [parse(line) for line in open("input/15").read().split('\n')]


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# interval trick by https://www.youtube.com/watch?v=OG1QwJ2RKsU


def part1():
    row = 2000000
    intervals = []
    beacon_xs = set()
    for (sensor, beacon) in items:
        d = distance(sensor, beacon)
        offset = d - abs(sensor[1] - row)
        min_x = sensor[0] - offset
        max_x = sensor[0] + offset
        if beacon[1] == row: 
            beacon_xs.add(beacon[0])
        intervals.append([min_x, max_x])

    impossible = set()    

    for min_x, max_x in intervals:
        for x in range(min_x, max_x + 1):
            impossible.add(x)
    
    print(len(impossible - beacon_xs))


def part2():
    MAX = 4000000

    for row in range(MAX):
        intervals = []

        for sensor, beacon in items:
            dist = distance(sensor, beacon)

            offset = dist - abs(sensor[1] - row)
            if offset < 0:
                continue
            min_x = sensor[0] - offset
            max_x = sensor[0] + offset

            intervals.append([min_x, max_x])

        intervals.sort()

        merged_intervals = [intervals[0]]

        for next_min, next_max in intervals[1:]:
            _, current_max = merged_intervals[-1]
            if next_min > current_max + 1:
                merged_intervals.append([next_min, next_max])
            else:
                merged_intervals[-1][1] = max(current_max, next_max)

        x = 0
        for min_x, max_x in merged_intervals:
            if x < min_x:
                print(x * 4000000 + row)
                exit(0)
            x = max(x, max_x + 1)
            if x > MAX:
                break


part1()
part2()
