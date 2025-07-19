import math
n = int(input())
ans = float('inf')
for w in range(1, int(math.isqrt(n)) + 2):
    h = (n + (w + 1) - 1) // (w + 1) - 1
    if h < 1: h = 1
    p = 2 * (w + h)
    if p < ans: ans = p
print(ans)
