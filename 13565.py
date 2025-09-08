import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().rstrip().split())

board = []
visited = [[False] * N for _ in range(M)]

for _ in range(M):
    data = str(input().rstrip())
    data = list(map(int, data))
    board.append(data)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

starts = []
for i, x in enumerate(board[0]):
    if x == 0:
        starts.append((0, i))

dq = deque(starts)
result = "NO"

while dq:
    cr, cc = dq.popleft()
    if visited[cr][cc]:
        continue
    if (cr == M - 1) and (board[cr][cc] == 0):
        result = "YES"
        break
    visited[cr][cc] = True
    
    for dr, dc in directions:
        nr, nc = cr + dr, cc + dc
        if (0 <= nr < M) and (0 <= nc < N) and not visited[nr][nc] and board[nr][nc] == 0:
            dq.append((nr, nc))
    
print(result)