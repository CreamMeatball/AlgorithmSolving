import sys

input = sys.stdin.readline

N = int(input().rstrip())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

# addPointByShape = {
#     0: [(0,1,0), (1,1,2)], # horizon
#     1: [(1,0,1), (1,1,2)], # vertical
#     2: [(0,1,0), (1,0,1), (1,1,2)] # diagonal
# }

dp = [[[0] * N for _ in range(N)] for _ in range(3)]
dp[0][0][1] = 1

# 일단 문제 잘 읽기.
# '꼭 빈 칸이어야 하는 곳은 색으로 표시되어져 있다.'
# 문제에서 색칠된 부분이 모두 빈칸이어야지만 해당 이동이 가능하다는 뜻임.
# 이 부분 꼭 확인하기.

for i in range(N):
    for j in range(N):
        for shape in range(3): # 모든 모양에 대해 순차적으로 한 번씩. shape: 현재 state의 모양
            if dp[shape][i][j] == 0: # 불가능한 경우 스킵
                continue
            
            # 가로 형태로 이동되어지는 가능한 경우
            if shape == 0 or shape == 2: # 가로, 대각선 -> 가로
                if j+1 < N and board[i][j+1] == 0:
                    dp[0][i][j+1] += dp[shape][i][j]
            # 세로 형태로 이동되어지는 가능한 경우
            if shape == 1 or shape == 2: # 세로, 대각선 -> 세로
                if i+1 < N and board[i+1][j] == 0:
                    dp[1][i+1][j] += dp[shape][i][j]
            # 대각선 형태로 이동되어지는 가능한 경우
            if i+1 < N and j+1 < N:
                if board[i][j+1] == 0 and board[i+1][j] == 0 and board[i+1][j+1] == 0:
                    dp[2][i+1][j+1] += dp[shape][i][j]
                    
            # 위 코드를 아래 형태로도 표현 가능. 근데 더 길어짐.
            # for i in range(N):
            #   for j in range(N):
            #       for shape in range(3):
            #           if shape == 0:
            #               # code ...
            #           if shape == 1:
            #               # code ...
            #           if shape == 2:
            #               # code ...
            
# for c in range(3):
#     print(f"for {['horizon','vertical','diagonal'][c]}")
#     for d in dp[c]:
#         print(d)
        
print(sum(dp[x][N - 1][N - 1] for x in range(3)))