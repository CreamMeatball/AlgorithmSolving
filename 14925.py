import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
dp = [[0] * N for _ in range(M)] # 만들 수 있는 정사각형의 '가장 큰 한 변 길이'
max_l = 0

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 # 정사각형을 만들어야하니 가장 짧은 길이로 제한이 걸림.
            
            if dp[i][j] > max_l:
                max_l = dp[i][j]

print(max_l)