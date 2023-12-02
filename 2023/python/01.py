import itertools
import re

lookup = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def valid_prefix(string):
    for k, _ in lookup:
        if k.startswith(string):
            return True
    return False


def parse_p1(string):
    first = next(itertools.dropwhile(lambda c: not c.isdigit(), string))
    last = next(itertools.dropwhile(lambda c: not c.isdigit(), reversed(string)))
    return int(first + last)


def get_digit(string, rev=False):
    i = 1
    n = 0
    d = None
    s = string
    while d is None:
        if valid_prefix(s[n:i]):
            d = lookup.get(s[n:i])
        else:
            n += 1
            i = 1

    return d

# If you try to extract both values with a single regex, it won't work: /(\d|one|two|...|nine)(?:.*(\d|one|two|...|nine))?/

regex = re.compile(r"(\d|one|two|three|four|five|six|seven|eight|nine)(:?.*(\d|one|two|three|four|five|six|seven|eight|nine))?")


def parse_p2(string):
    matches = regex.search(string).groups()
    first_digit = matches[0]
    last_digit = matches[-1]
    print(f"{string} ---> {first_digit}     {last_digit}")
    return int(
        lookup.get(first_digit, first_digit) + lookup.get(last_digit, last_digit)
    )


with open("input/01.txt") as f:
    input = f.readlines()

    p1 = sum(map(parse_p1, input))
    p2 = sum(map(parse_p2, input))

    print(p1)
    print(p2)
