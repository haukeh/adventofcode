G = []


def parse_cubes(string):
    def pairs(s):
        g = {}
        for pair in s.split(","):
            cnt, cube = pair.strip().split(" ")
            g[cube] = int(cnt)
        return g

    return [pairs(l) for l in string.split(";")]


def parse(string):
    _, plays = string.strip().split(":")
    G.append(parse_cubes(plays))


def possible(play):
    LIM = {"red": 12, "green": 13, "blue": 14}
    for cube, amnt in play.items():
        if amnt > LIM[cube]:
            return False

    return True


with open("input/02.txt") as f:
    lines = f.readlines()

    for line in lines:
        parse(line)

    sum_possible = 0
    power = 0
    for i, game in enumerate(G):
        mb= mr = mg = 0
        p = True
        for play in game:
            if not possible(play):
                p = False
            mb = max(play.get("blue", 0), mb)
            mr = max(play.get("red", 0), mr)
            mg = max(play.get("green", 0), mg)

        if p:
            sum_possible += i + 1
        power += mb * mr * mg

    print(sum_possible)
    print(power)
