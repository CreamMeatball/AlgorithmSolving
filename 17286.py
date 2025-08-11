import sys
import math
from itertools import permutations

input = sys.stdin.readline

def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

data = [tuple(map(int, input().rstrip().split())) for _ in range(4)]
start = data[0]
people = data[1:]

best = float('inf')
for order in permutations(people):
    total = dist(start, order[0]) + dist(order[0], order[1]) + dist(order[1], order[2])
    best = min(best, total)

print(math.floor(best))