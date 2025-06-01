import sys
from itertools import combinations

input_ = sys.stdin.readline

N = int(input_().rstrip())
ropes = []
for _ in range(N):
    ropes.append(int(input_().rstrip()))
    
# greedy    
ropes.sort(reverse=True)

max_weight = 0

for i in range(0, N):
    # print(f"ropes[i]: {ropes[i]}")
    current_weight = ropes[i] * (i + 1)
    max_weight = max(current_weight, max_weight)
    
print(max_weight)