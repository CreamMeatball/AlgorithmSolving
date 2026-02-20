import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
r1, c1, r2, c2 = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]

dist = [[-1] * M for _ in range(N)]
dq = deque([(r1 - 1, c1 - 1)])
dist[r1 - 1][c1 - 1] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 0-1 BFS

while dq:
    r, c = dq.popleft()
    
    if r == r2 - 1 and c == c2 - 1:
        print(dist[r][c])
        break
        
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < M and dist[nr][nc] == -1:
            if board[nr][nc] == '0':
                dist[nr][nc] = dist[r][c] # 0일 때는 거리를 안 늘리고
                dq.appendleft((nr, nc)) # 0일 경우를 앞단에 넣어서 먼저 처리
            else:
                dist[nr][nc] = dist[r][c] + 1 # 1일 때만 거리(cost)를 늘림
                dq.append((nr, nc)) # 1일 경우는 뒷단에 넣어서 나중에 처리