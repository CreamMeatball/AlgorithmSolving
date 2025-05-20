import sys
from collections import deque

input_ = sys.stdin.readline
testPrint = False
N, M = map(int, input_().split())

# bfs + kruskal
# kruskal에서 가중치를 다리 길이로 보는 것.

map_ = [[-1] * (M + 2)]
for _ in range(N):
    map_.append([-1] + list(map(int, input_().split())) + [-1])
map_.append([-1] * (M + 2))

# 섬 번호 기록용
island_map = [[-1] * (M + 2)]
for _ in range(N):
    island_map.append([-1] + [0] * (M) + [-1])
island_map.append([-1] * (M + 2))
visited    = [[False] * (M + 2) for _ in range(N + 2)]
direction  = [(-1, 0), (1, 0), (0, -1), (0, 1)]

island_index = 1

def bfs(init_x, init_y, idx):
    queue = deque([(init_x, init_y)])
    visited[init_x][init_y] = True
    island_map[init_x][init_y] = idx
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if not visited[nx][ny] and map_[nx][ny] == 1:
                visited[nx][ny] = True
                island_map[nx][ny] = idx
                queue.append((nx, ny))

# 1) 섬 번호 매기기 (bfs)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if map_[i][j] == 1 and not visited[i][j]:
            bfs(i, j, island_index)
            island_index += 1

if testPrint:
    print("island_map: ")
    for row in island_map:
        print(row)

# 2) a땅 <-> b땅 가는 최소의 다리 길이 찾기
INF = 10**9
edges = {}   # key=(a,b), value=최소 길이
island_valid = [False] * (island_index) # island_index가 이미 +1 된 상태
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
                    b = island_map[x][y] # 다른 땅에 다다랐을 때
                    if b != a and length >= 2:
                        key = (a, b) if a < b else (b, a)
                        island_valid[a] = True; island_valid[b] = True
                        edges[key] = min(edges.get(key, INF), length) # key값 (a, b)의 값(a<->b)을 최소값으로 설정
                    break

if testPrint:
    print("edges: ")
    print(edges)
    
if testPrint:
    print("island_valid: ")
    print(island_valid)
    
for v in island_valid[1:]:
    if not v:
        print(-1)
        sys.exit()

# 3) Kruskal을 위한 간선 리스트 생성 및 정렬
edge_list = sorted((length, a, b) for (a,b), length in edges.items())

if testPrint:
    print("edges_list: ")
    print(edge_list)

parent = list(range(island_index)) # island_index가 이미 +1 된 상태
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(a, b):
    root_a, root_b = find(a), find(b)
    if root_a != root_b:
        parent[root_b] = root_a

# 4) MST 구하기
def kruskal(edge_list):
    total_min_length, edge_count = 0, 0
    for e in edge_list:
        length, a, b = e
        print(f"(a, b): {a, b}, length: {length}") if testPrint else None
        if find(a) != find(b):
            union(a, b)
            total_min_length += length
            edge_count += 1
    return total_min_length, edge_count
            
total_min_length, edge_count = kruskal(edge_list)
if edge_count != island_index - 2: # 예를 들어, 네 섬 중 두 섬끼리만 연결돼있고 전체 연결은 되어있지 않은 경우
    print(-1)
    sys.exit()
print(total_min_length)