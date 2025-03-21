import sys

input_data = sys.stdin.readline

n = int(input_data().rstrip())
m = int(input_data().rstrip())
    
# 모든 도시에 대해 출력해야하니
# Floyd-Warshall 알고리즘 써야할 듯

graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
route = [[0] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    u, v, w = map(int, input_data().split())
    graph[u][v] = min(graph[u][v], w)  # 여러 버스 중 최소 비용 선택

# Floyd-Warshall
for k in range(1, n + 1): # k: 경유해가는 노드
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                route[a][b] = k

# 경로 재구성
def reconstruct_path(start, end):
    if route[start][end] == 0:
        return [] if start == end else [start, end]
    
    mid = route[start][end]
    path1 = reconstruct_path(start, mid)
    path2 = reconstruct_path(mid, end)
    return path1[:-1] + path2  # 중복 노드 제거

# 거리 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if graph[i][j] == float('inf') else graph[i][j], end=' ')
    print()

# 경로 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j or graph[i][j] == float('inf'):
            print(0)
            continue
        
        path = reconstruct_path(i, j)
        print(len(path), end=' ')
        print(' '.join(map(str, path)))