import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]
MOD = 1000000009

dp = [0] * M
for i in range(N):
    row = grid[i]
    for j in range(M):
        res = 1
        if i > 0:
            p = grid[i-1][j]
            if p == 'S' or p == 'B':
                res += dp[j]
        if j > 0:
            p = row[j-1]
            if p == 'E' or p == 'B':
                res += dp[j-1]
        dp[j] = res % MOD

print(dp[M-1])
