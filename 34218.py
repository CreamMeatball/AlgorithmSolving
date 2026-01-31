import sys
from collections import deque

N, M = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))
    
# 출발지, 에서 걸어서 갈 수 있는 모든 영역을 한 덩어리의 A영토로 표시
# 도착지, 에서 걸어서 갈 수 있는 모든 영역을 한 덩어리의 B영토로 표시
# (flood-fill)

# 그럼 A영토에서 B영토로 텔포 타는 최소 거리는 어떻게 계산하냐:
# A영토의 테두리에서 사방으로 확장해서 영토를 키워봄
# BFS로 queue에 넣은 다음에, 사방으로 확장하다가 B영토에 닿는 순간, 그 때가 제일 최단거리임

# 1-based -> 0-based
sr, sc = map(int, input().rstrip().split())
sr, sc = sr - 1, sc - 1
er, ec = map(int, input().rstrip().split())
er, ec = er - 1, ec - 1

# 영역 표시를 위한 배열 (-1: 미방문, 0: A영토, 1: B영토)
territory = [[-1] * M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def flood_fill(start_r, start_c, type_id):
    q = deque([(start_r, start_c)])
    territory[start_r][start_c] = type_id
    group = [(start_r, start_c)]
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 1 and territory[nr][nc] == -1:
                territory[nr][nc] = type_id
                q.append((nr, nc))
                group.append((nr, nc))
    return group

# 출발지에서 걸어서 갈 수 있는 A영토 표시
group_a = flood_fill(sr, sc, 0)

# 만약 입구와 출구가 이미 같은 영역이라면 걸어갈 수 있으니 마나 0 소모
if territory[er][ec] == 0:
    print(0)
    sys.exit()

# 도착지에서 걸어서 갈 수 있는 B영토 표시
group_b = flood_fill(er, ec, 1)

# A영토에서 B영토로 가는 최소 텔레포트 거리 계산 (다중 시작점 BFS)
dist = [[-1] * M for _ in range(N)]
q = deque()

for r, c in group_a:
    dist[r][c] = 0
    q.append((r, c))
    
while q:
    r, c = q.popleft()
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < M:
            # B영토를 만나면, 그 때가 최소.
            if territory[nr][nc] == 1:
                print(dist[r][c] + 1)
                sys.exit()
            
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))