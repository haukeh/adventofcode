from functools import reduce


def sim(races):
    res = 1
    for (t, record) in races:                 
        wins = 0
        for hold in range(1, t): 
            rest = t - hold
            traveled = rest * hold 
            if traveled > record: 
                wins += 1
        res *= wins
    return res
        

            

with open("input/06.txt") as f: 
    lines = f.readlines()
    times = [int (x) for x in lines[0].split(":")[1].split()]
    dists = [int (x) for x in lines[1].split(":")[1].split()]
    
    races = list(zip(times, dists))
    
    time = int(reduce(lambda a, b: str(a) + str(b), times))
    dist = int(reduce(lambda a, b: str(a) + str(b), dists))

    p1 = sim(races)
    print(p1)
    
    p2 = sim([(time, dist)])
    print(p2)