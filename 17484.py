N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

for j in range(M):
    for k in range(3):
        dp[0][j][k] = matrix[0][j]

for i in range(1, N):
    for j in range(M):
        if j + 1 < M:
            dp[i][j][0] = matrix[i][j] + min(dp[i-1][j+1][1], dp[i-1][j+1][2])
        
        dp[i][j][1] = matrix[i][j] + min(dp[i-1][j][0], dp[i-1][j][2])
        
        if j - 1 >= 0:
            dp[i][j][2] = matrix[i][j] + min(dp[i-1][j-1][0], dp[i-1][j-1][1])

ans = INF
for j in range(M):
    ans = min(ans, min(dp[N-1][j]))

print(ans)