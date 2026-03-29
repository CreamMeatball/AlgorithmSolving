import sys

input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))

p = [0] * (n + 1)
for i in range(n):
    p[i+1] = p[i] + t[i]

ans = 0
for i in range(m, n + 1):
    val = p[i] - p[i-m]
    if val > ans:
        ans = val

print(ans)