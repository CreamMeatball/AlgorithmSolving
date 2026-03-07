import sys

input = sys.stdin.readline

dp = [[0] * 211 for _ in range(21)]
dp[0][0] = 1

for i in range(1, 21):
    for j in range(211):
        for m in range(i + 1):
            if j >= m:
                dp[i][j] += dp[i-1][j-m]

t = int(input().rstrip())
for _ in range(t):
    k, n = map(int, input().split())
    if n < 0 or n > 210:
        print(0)
    else:
        print(dp[k][n])
