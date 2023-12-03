import itertools

lookup = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def valid_prefix(string): 
    res = False 
    for k, _ inf

def parse_p1(string):
    first = next(itertools.dropwhile(lambda c: not c.isdigit(), string))
    last = next(itertools.dropwhile(lambda c: not c.isdigit(), reversed(string)))
    return int(first + last)


def get_digit(string, rev=False):
    i = 1
    d = None

    while d is None:
        chars = string[:i]
        d = lookup.get(chars if not rev else reversed(chars))

    return d


def parse_p2(string):
    first_digit = get_digit(string)
    last_digit = get_digit(reversed(string), rev=True)

    return int(str(first_digit) + str(last_digit))

with open("input/01.txt") as f:
    input = f.readlines()

    p1 = sum(map(parse_p1, input))
    p2 = sum(map(parse_p2, input))

    print(p1)
    print(p2)
