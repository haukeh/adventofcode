with open('in/day5a.txt') as f:
    raw_in = f.readline().strip()

i = 0
while i < len(raw_in) - 1:
    if ord(raw_in[i]) == (ord(raw_in[i + 1]) + 32) or ord(raw_in[i]) == (ord(raw_in[i + 1]) - 32):
        raw_in = raw_in[:i] + raw_in[i + 2:]
        i = max(0, i - 2)
    else:
        i = i + 1

print(len(raw_in))
