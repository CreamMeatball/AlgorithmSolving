# PyPy3 because of time exceeding

import sys

input = sys.stdin.readline

N = int(input().rstrip())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

dp = [[1] * N for _ in range(N)]

# 부분수열은 꼭 완전히 이어져있지 않아도 됨. 건너뛰어도 됨.
# * 이어져있어야하는 건 '연속'된 부분 수열

for i in range(N): # 현재 행
    for j in range(N): # 현재 열
        for r in range(i + 1): # 이전 행
            for c in range(j + 1): # 이전 열
                if board[r][c] < board[i][j]:
                    dp[i][j] = max(dp[i][j], dp[r][c] + 1)

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dp[i][j])

print(ans)