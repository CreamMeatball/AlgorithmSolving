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

bus = {}
for _ in range(m):
    u, v, w = map(int, input_data().split())
    if u not in bus:
        bus[u] = []
    bus[u].append((v, w))
    graph[u][v] = w

for k in range(1, n + 1): # k: 경유해가는 노드
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0
                continue
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                route[k][b] = a
                
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(graph[a][b], end=' ')
    print()
print()
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(route[a][b], end=' ')
    print()
print()