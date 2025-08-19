import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(start: tuple, board: list, visited):
    dq = deque([start])
    visited[start[0]][start[1]] = True
    will_melt = []
    # visited = [[False] * M for _ in range(N)]
    count = 0 # 몇 개 영토 탐색했는지
    while dq:
        r, c = dq.popleft()
        count += 1
        # 주변 물 탐색
        water = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < N) and (0 <= nc < M) and board[nr][nc] == 0:
                water += 1
        will_melt.append((r, c, water))
        
        # 주변 확장
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < N) and (0 <= nc < M) and board[nr][nc] != 0 and not visited[nr][nc]:
                dq.append((nr, nc))
                visited[nr][nc] = True
        
    return count, will_melt, visited

ice = [] # 얼음이 존재하는 위치

for i in range(N):
    for j in range(M):
        if board[i][j] != 0:
            ice.append((i,j))
            
ice_count = int(len(ice)) # 잔여 얼음 수

trigger = True

year = 0

while trigger:
    visited = [[False] * M for _ in range(N)]
    not_searced_ice_count = int(len(ice))
    group_count = 0
    year += 1
    melts = [] # 이번 년도에 녹을 좌표와 양을 모아둠
    for ice_r, ice_c in ice:
        if visited[ice_r][ice_c]:
            continue
        count, will_melt, visited_updated = bfs((ice_r, ice_c), board, visited)
        visited = visited_updated
        group_count += 1
        melts.extend(will_melt)
        not_searced_ice_count -= count
        if not_searced_ice_count <= 0:
            break

    # 녹이기 적용 — ice 리스트는 나중에 재구성
    for melt_r, melt_c, water in melts:
        board[melt_r][melt_c] = max(0, board[melt_r][melt_c] - water)

    # ice 리스트와 ice_count 재구성
    ice = [(i, j) for i in range(N) for j in range(M) if board[i][j] != 0]
    ice_count = len(ice)
    
print(year)