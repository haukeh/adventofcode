with open('in/day5a.txt') as f:
    input = f.readline()


def scan(string):
    for i, c in enumerate(input):
        if i + 1 > len(input):
            break

        if ord(c) == (ord(input[i + 1]) + 32) or ord(c) == (ord(input[i + 1]) - 32):
            return scan(input[:i - 1] + input[i + 1:])

    return string


print(scan(input))