from collections import deque

N = int(input())

# board = [[0 for _ in range(N)] for _ in range(N)]
board = deque()
for _ in range(N):
    board.append([0 for _ in range(N)])

def queen(y, x):
    for i in range(N):
        board[y][i] += 1
        board[i][x] += 1
        if 0 <= y + i < N and 0 <= x + i < N:
            board[y + i][x + i] += 1
        if 0 <= y - i < N and 0 <= x - i < N:
            board[y - i][x - i] += 1
        if 0 <= y + i < N and 0 <= x - i < N:
            board[y + i][x - i] += 1
        if 0 <= y - i < N and 0 <= x + i < N:
            board[y - i][x + i] += 1

def unqueen(y, x):
    for i in range(N):
        board[y][i] -= 1
        board[i][x] -= 1
        if 0 <= y + i < N and 0 <= x + i < N:
            board[y + i][x + i] -= 1
        if 0 <= y - i < N and 0 <= x - i < N:
            board[y - i][x - i] -= 1
        if 0 <= y + i < N and 0 <= x - i < N:
            board[y + i][x - i] -= 1
        if 0 <= y - i < N and 0 <= x + i < N:
            board[y - i][x + i] -= 1
            
def dfs(depth):
    if depth == N:
        return 1
    result = 0
    for i in range(N):
        if board[depth][i] == 0:
            queen(depth, i)
            result += dfs(depth + 1)
            unqueen(depth, i)
    return result

print(dfs(0))