from collections import defaultdict


class Particle:
    def __init__(self, id, p, v, a):
        self.id = id
        self.p = p
        self.v = v
        self.a = a

    def step(self):
        for i in range(3):
            print(i)
            self.v[i] += self.a[i]
            self.p[i] += self.v[i]

    def __str__(self) -> str:
        return '[{3}] p: {0}, v: {1}, a: {2}'.format(self.p, self.v, self.a,
                                                     self.id)


def parse(idx, line):
    parts = line.split()
    res = []
    for part in parts:
        res.append([int(sub) for sub in
                    part[part.index('<') + 1:part.index('>')].split(',')])

    return Particle(idx, p=res[0], v=res[1], a=res[2])


with open('../resources/day20.input') as f:
    particles = [parse(i, l) for i, l in enumerate(f)]

    for i in range(0, 40):
        for ptcl in particles:
            ptcl.step()

        nxt = []
        groups = defaultdict(list)
        for ptcl in particles:
            groups[tuple(ptcl.p)].append(ptcl)

        for k, v in groups.items():
            if len(v) == 1:
                nxt.extend(v)

        particles = nxt

    print(len(particles))

    # PART 1:
    #
    # particles.sort(key=lambda particle: (
    #     math.fsum(map(abs, particle.a)), math.fsum(map(abs, particle.v)),
    #     math.fsum(map(abs, particle.p))))
    #
    # for i in range(0, 10):
    #     print(particles[i])
