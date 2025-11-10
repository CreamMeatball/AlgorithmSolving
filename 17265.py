import sys

input = sys.stdin.readline

N = int(input().rstrip())

board = []

for _ in range(N):
    board.append(list(map(str, input().rstrip().split())))

max_dp = [[-float('inf')] * N for _ in range(N)]
min_dp = [[float('inf')] * N for _ in range(N)]

def op(a, b, i, j):
    if board[i][j] == '*':
        return int(a) * int(b)
    if board[i][j] == '+':
        return int(a) + int(b)
    if board[i][j] == '-':
        return int(a) - int(b)
    
def process_na(i, j):
    if i == 0:
        max_dp[i][j] = max_dp[i][j - 1]
        min_dp[i][j] = min_dp[i][j - 1]
    elif j == 0:
        max_dp[i][j] = max_dp[i - 1][j]
        min_dp[i][j] = min_dp[i - 1][j]
    else:
        max_dp[i][j] = max(max_dp[i - 1][j], max_dp[i][j - 1])
        min_dp[i][j] = min(min_dp[i - 1][j], min_dp[i][j - 1])

def process_row(i, j):
    is_number = 1 if (i + j) % 2 == 0 else 0
    if is_number:
        max_dp[i][j] = max(max_dp[i][j], op(max_dp[i - 1][j], int(board[i][j]), i - 1, j))
        min_dp[i][j] = min(min_dp[i][j], op(min_dp[i - 1][j], int(board[i][j]), i - 1, j))
    else:
        process_na(i, j)
        
def process_col(i, j):
    is_number = 1 if (i + j) % 2 == 0 else 0
    if is_number:
        max_dp[i][j] = max(max_dp[i][j], op(max_dp[i][j - 1], int(board[i][j]), i, j - 1))
        min_dp[i][j] = min(min_dp[i][j], op(min_dp[i][j - 1], int(board[i][j]), i, j - 1))
    else:
        process_na(i, j)

for i in range(N):
    for j in range(N):
        is_number = 1 if (i + j) % 2 == 0 else 0
        
        if i == 0 and j == 0:
            max_dp[i][j] = int(board[i][j])
            min_dp[i][j] = int(board[i][j])
            continue
        elif i == 0:
            process_col(i, j)
        elif j == 0:
            process_row(i, j)
        else:
            process_row(i, j)
            process_col(i, j)
            
print(max_dp[N - 1][N - 1], min_dp[N - 1][N - 1])