import sys
import math
from collections import defaultdict

input = sys.stdin.readline

N = int(input().rstrip())
count = defaultdict(int)

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    g = math.gcd(abs(x), abs(y)) # 비율 (각도) 를 계산하기 위해
    dx, dy = x // g, y // g 
    count[(dx, dy)] += 1

print(max(count.values()))