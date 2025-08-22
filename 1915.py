import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

board = []
for _ in range(n):
    board.append(list(int(x) for x in str(input().rstrip())))
    
# print(board)

# 생각하기가 어려움
# -> DP 어려울 때 직접 케이스 그려보기.
# -> 실제 예시 보고 귀납적으로 점화식 도출.

# [참고]
# https://kyun2da.github.io/2021/04/09/biggestSquare/

# dp[i][j]: (i, j)를 오른쪽 아래 꼭짓점으로 하는 가장 큰 정사각형의 한 변의 길이라고 할 때
# - 2x2 list 일 때
#  <list>          <dp>
# [[1 1].        [[1 1]
#  [1 1]].  ->.   [1 2]]

# - 3x3 list 일 때
#  <list>             <dp>
# [[1 1 1].         [[1 1 1]
#  [1 1 1].  ->.     [1 2 2]
#  [1 1 1]]          [1 2 3]]  

# - 4x4 list 일 때
#   <list>               <dp>
# [[1 1 1 1].         [[1 1 1 1]
#  [1 1 1 1].   ->.    [1 2 2 2]
#  [1 1 1 1].          [1 2 3 3]  
#  [1 1 1 1]]          [1 2 3 4]]

# => 점화식:
# dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

dp = [[0] * m for _ in range(n)]

max_len = 0

# 가장 윗 행과 가장 왼쪽 열에 대한 dp값 초기화
dp[0] = [x for x in board[0]]
max_len = max(dp[0])
for j in range(1, n):
    dp[j][0] = board[j][0]
    max_len = max(max_len, dp[j][0])
    
    
for i in range(1, n):
    for j in range(1, m):
        if board[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        max_len = max(max_len, dp[i][j])
        
print(max_len ** 2)