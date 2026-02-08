import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(M)]
cnt = 0
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            cnt += 1
            q = deque([(i, j)])
            graph[i][j] = 0
            while q:
                x, y = q.popleft()
                for k in range(8):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        q.append((nx, ny))
print(cnt)
