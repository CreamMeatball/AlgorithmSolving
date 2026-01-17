import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
g = [list(map(int, input().rstrip().split())) for _ in range(n)]
q = deque()

for r in range(n):
    for c in range(m):
        if g[r][c] == 1:
            q.append((r, c))

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

ans = 0
while q:
    r, c = q.popleft()
    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and g[nr][nc] == 0:
            g[nr][nc] = g[r][c] + 1
            ans = max(ans, g[nr][nc])
            q.append((nr, nc))

print(ans - 1)
