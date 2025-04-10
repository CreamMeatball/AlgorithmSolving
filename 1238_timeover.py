import sys

input_data = sys.stdin.readline

N, M, X = map(int, input_data().rstrip().split())

graph = {}

# floyd-warshall

INF = float('inf')

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input_data().rstrip().split())
    graph[u][v] = w
    
min_time = [INF] * (N + 1)
min_time[X] = 0
    
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            if j == X and (graph[i][j] + graph[j][i]) < min_time[i]:
                min_time[i] = graph[i][j] + graph[j][i]

# print(min_time[1:])
print(max(min_time[1:]))