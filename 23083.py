import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
h = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
    r, c = map(int, input().split())
    h[r][c] = 1

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[1][1] = 1

MOD = 1000000007

for j in range(1, M + 1):
    for i in range(1, N + 1):
        if h[i][j] or (i == 1 and j == 1):
            continue
        
        v = dp[i-1][j]
        if j > 1:
            if j % 2 == 0:
                v += dp[i][j-1]
                if i < N: v += dp[i+1][j-1]
            else:
                v += dp[i][j-1] + dp[i-1][j-1]
        dp[i][j] = v % MOD

print(dp[N][M])