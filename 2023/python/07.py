from collections import Counter
import functools
import itertools


def card_value(c):
    match c:
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "J":
            return 11
        case "T":
            return 10
        case i:
            return int(i)


def card_value2(c):
    match c:
        case "A":
            return 14
        case "K":
            return 13
        case "Q":
            return 12
        case "J":
            return 1
        case "T":
            return 10
        case i:
            return int(i)


def get_type(hand):
    c = Counter(hand)
    mc = c.most_common()[0]
    if mc[1] == 5:
        return 6
    elif mc[1] == 4:
        return 5
    elif mc[1] == 3:
        if len(c.most_common()) == 2:
            return 4
        else:
            return 3
    elif mc[1] == 2:
        num_pairs = 1
        rest = c.most_common()[1:]
        for _, n in rest:
            if n == 2:
                num_pairs += 1

        return 2 if num_pairs == 2 else 1
    else:
        return 0


def tie(a, b):
    c = list(itertools.dropwhile(lambda t: t[0] == t[1],  zip(a, b)))

    (aa, bb) = c[0]

    if card_value(aa) > card_value(bb):
        return 1
    else:
        return -1


def tie2(a, b):
    c = list(itertools.dropwhile(lambda t: t[0] == t[1],  zip(a, b)))

    (aa, bb) = c[0]

    if card_value2(aa) > card_value2(bb):
        return 1
    else:
        return -1


def cmp(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        return tie(a[1], b[1])

def cmp2(a, b):
    if a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        return tie2(a[1], b[1])

def p1():
    with open("input/07.txt") as f:
        items = []
        for line in f.readlines():
            cards, bet = line.strip().split()
            type = get_type(cards)
        
        res = sorted(items, key=functools.cmp_to_key(cmp))

        # print("\n".join(map(str, res)))

        a = 0
        for i, c in enumerate(res, 1):
            a += i * int(c[2])

        print(a)


def p2():
    with open("input/07.txt") as f:
        items = []
        for line in f.readlines():                        
            cards, bet = line.strip().split()

            jokers = cards.count("J")

            if jokers == 0:
                type = get_type(cards)
                items.append((type, cards, bet))
            else:
                ranks = set()
                for perms in itertools.combinations_with_replacement("AKQT98765432", jokers):
                    replaced = cards
                    for c in perms:
                        replaced = replaced.replace("J", c, 1)            
                    rank = get_type(replaced)
                    ranks.add(rank)
                    if rank == 6:
                        break
                mx_rank = max(ranks)
                items.append((mx_rank, cards, bet))


        res = sorted(items, key=functools.cmp_to_key(cmp2))

        a = 0
        for i, c in enumerate(res, 1):
            a += i * int(c[2])

        print(a)


p2()