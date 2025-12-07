import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

numbers = list(map(int, input().split()))

dp = [[[-float('inf')] * 2 for _ in range(M + 1)] for _ in range(N + 1)]

dp[0][0][0] = 0

for i in range(1, N + 1):
    num = numbers[i-1]
    
    for j in range(M + 1):
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])

        if j > 0:
            extend_group = dp[i-1][j][1] + num
            start_new_group = max(dp[i-1][j-1][0], dp[i-1][j-1][1]) + num
            dp[i][j][1] = max(extend_group, start_new_group)

result = max(dp[N][M][0], dp[N][M][1])
print(result)