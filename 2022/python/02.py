p1 = 0
p2 = 0
p1_scores = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1,
             'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}
p2_scores = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1,
             'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}

for l in open('input/02').read().split('\n'):
    p1 += p1_scores[l]
    p2 += p2_scores[l]

print(f'p1 {p1}')
print(f'p2 {p2}')