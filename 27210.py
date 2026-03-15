import sys
input = sys.stdin.readline

# 카데인 알고리즘

N = int(input().rstrip())
arr = list(map(int, input().split()))

max_val = 0
min_val = 0
curr_max = 0
curr_min = 0

for x in arr:
    v = 1 if x == 1 else -1
    
    curr_max += v
    if curr_max < 0:
        curr_max = 0
    if curr_max > max_val:
        max_val = curr_max
        
    curr_min += v
    if curr_min > 0:
        curr_min = 0
    if curr_min < min_val:
        min_val = curr_min

print(max(max_val, abs(min_val)))
