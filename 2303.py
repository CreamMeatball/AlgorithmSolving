import sys
from itertools import combinations

input_ = sys.stdin.readline

N = int(input_().rstrip())

cards = []
for _ in range(N):
    cards.append(list(map(int, input_().rstrip().split())))
    
max_sum = [0 for _ in range(N)]
max_total_sum = 0
max_i = -1
for i in range(N):
    comb = combinations(cards[i], 3)
    for c in comb:
        current_sum = int(sum(c)) % 10
        max_sum[i] = max(max_sum[i], current_sum)
        # print(f"i: {i}, max_sum[i]: {max_sum[i]}")
        if max_total_sum <= max_sum[i]:
            max_total_sum = max_sum[i]
            max_i = i
            
print(max_i + 1)