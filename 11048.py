N, M = map(int, input().split())

candy = []
for _ in range(N):
    candy.append(list(map(int, input().split())))

dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        current_candy = candy[i][j]
        from_top = 0
        if i > 0:
            from_top = dp[i-1][j]
        from_left = 0
        if j > 0:
            from_left = dp[i][j-1]
        from_diag = 0
        if i > 0 and j > 0:
            from_diag = dp[i-1][j-1]

        dp[i][j] = current_candy + max(from_top, from_left, from_diag)
        
print(dp[N-1][M-1])