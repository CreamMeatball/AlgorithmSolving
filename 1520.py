import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dp = [[-1] * N for _ in range(M)] # 메모이제이션

def dfs(r, c):
    if r == M - 1 and c == N - 1:
        return 1
    
    if dp[r][c] != -1:
        return dp[r][c]
    
    ways = 0
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N and board[nr][nc] < board[r][c]:
            ways += dfs(nr, nc)
    
    dp[r][c] = ways
    return ways

print(dfs(0, 0))
