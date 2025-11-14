import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + board[i - 1][j - 1]
        # 아래 / 오른쪽으로 탐사하는 방식을, 그냥 dp[i - 1][j] or dp[i][j - 1] 중 max를 가져오는 방식으로 구현 가능

print(dp[N][M])