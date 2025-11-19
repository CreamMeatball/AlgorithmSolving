import sys

input = sys.stdin.readline

T = int(input().rstrip())

ns = list(int(input().rstrip()) for _ in range(T))

dp = [0] * (max(ns) + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, len(dp)):
    if (i - 1) >= 0:
        dp[i] += dp[i - 1]
    if (i - 2) >= 0:
        dp[i] += dp[i - 2]
    if (i - 3) >= 0:
        dp[i] += dp[i - 3]
        
for n in ns:
    print(dp[n])