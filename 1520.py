import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
board = []
for _ in range(M):
    board.append(list(input().rstrip().split()))
    
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
count = 0
start = (0, 0)

def dfs(current):
    global count
    r, c = current
    if r == M - 1 and c == N - 1:
        count += 1
    current_h = board[r][c]
    for d in directions:
        nr = r + d[0]
        nc = c + d[1]
        if (0 <= nr < M and 0 <= nc < N) and board[nr][nc] < current_h:
            dfs((nr, nc))
    return

dfs(start)
print(count)