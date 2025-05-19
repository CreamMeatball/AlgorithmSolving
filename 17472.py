import sys
from collections import deque

input_ = sys.stdin.readline
N, M = map(int, input_().split())

# bfs + kruskal
# kruskal에서 가중치를 다리 길이로 보는 것.

map_ = [[-1] * (M + 2)]
for _ in range(N):
    map_.append([-1] + list(map(int, input_().split())) + [-1])
map_.append([-1] * (M + 2))

# 섬 번호 기록용
island_map = [[0] * (M + 2) for _ in range(N + 2)]
visited    = [[False] * (M + 2) for _ in range(N + 2)]
direction  = [(-1, 0), (1, 0), (0, -1), (0, 1)]

island_index = 0

def bfs(init_x, init_y, idx):
    queue = deque([(init_x, init_y)])
    visited[init_x][init_y] = True
    island_map[init_x][init_y] = idx
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if not visited[nx][ny] and map_[nx][ny] == 1:
                visited[nx][ny]    = True
                island_map[nx][ny] = idx
                queue.append((nx, ny))

# 1) 섬 번호 매기기 (bfs)
for i in range(1, N+1):
    for j in range(1, M+1):
        if map_[i][j]==1 and not visited[i][j]:
            bfs(i, j, island_index)
            island_index += 1

# 2) 가능한 다리 모두 찾기
INF = 10**9
edges = {}   # key=(a,b), value=최소 길이
for i in range(1, N + 1):
    for j in range(1, M + 1):
        a = island_map[i][j]
        if a > 0:
            for dx, dy in direction:
                length = 0
                x, y = i, j
                while True:
                    x += dx
                    y += dy
                    if map_[x][y] == -1:
                        break
                    if island_map[x][y] == 0:
                        length += 1
                        continue
                    b = island_map[x][y]
                    if b != a and length >= 2:
                        key = (a, b) if a < b else (b, a)
                        edges[key] = min(edges.get(key, INF), length)
                    break

# 3) Kruskal을 위한 간선 리스트 생성 및 정렬
edge_list = sorted((L, a, b) for (a,b), L in edges.items())

parent = list(range(island_index))
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra

# 4) MST 구하기
res = 0
cnt = 0
for L, a, b in edge_list:
    if find(a) != find(b):
        union(a,b)
        res += L
        cnt += 1
        if cnt == island_index-1:
            break

# 5) 모든 섬이 연결됐는지 확인
roots = set(find(i) for i in range(island_index))
print(res if len(roots) == 1 else -1)