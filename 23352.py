# PyPy3

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 0이 아닌 방 목록
cells = [(i, j) for i in range(N) for j in range(M) if grid[i][j] != 0]

if not cells:
    print(0)
    sys.exit()

# 인접 리스트 미리 생성 (BFS 내부의 조건문과 범위 검사 횟수를 줄임)
adj = [[[] for _ in range(M)] for _ in range(N)]
for i, j in cells:
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] != 0:
            adj[i][j].append((ni, nj))

max_dist = -1
best_sum = 0

# 각 방에서 BFS
for si, sj in cells:
    dist = [[-1] * M for _ in range(N)]
    q = deque([(si, sj)])
    dist[si][sj] = 0
    start_val = grid[si][sj]

    while q:
        i, j = q.popleft()
        d = dist[i][j]

        # BFS 도중 도달한 방의 거리와 합을 바로 계산 (효율화)
        s = start_val + grid[i][j]
        
        if d > max_dist:
            max_dist = d
            best_sum = s
        elif d == max_dist:
            if s > best_sum:
                best_sum = s

        for ni, nj in adj[i][j]:
            if dist[ni][nj] == -1:
                dist[ni][nj] = d + 1
                q.append((ni, nj))

print(best_sum if max_dist >= 0 else 0)
