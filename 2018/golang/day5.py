import string
import sys

with open('in/day5a.txt') as f:
    raw_in = f.readline().strip()


def collapse(word):
    i = 0
    while i < len(word) - 1:
        if ord(word[i]) == (ord(word[i + 1]) + 32) or ord(word[i]) == (ord(word[i + 1]) - 32):
            word = word[:i] + word[i + 2:]
            i = max(0, i - 2)
        else:
            i = i + 1
    return word


print(len(collapse(raw_in)))

min_len = sys.maxsize

for cc in string.ascii_lowercase:
    min_len = min(len(collapse(''.join([c for c in raw_in if c.lower() != cc]))), min_len)

print(min_len)
