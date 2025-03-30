from itertools import combinations
from math import lcm

numbers = list(map(int, input().split()))

lcm_num = float('inf')

for comb in combinations(numbers, 3):
    cm = lcm(*comb) # unpack tuple
    if cm < lcm_num:
        lcm_num = cm
        
print(lcm_num)
