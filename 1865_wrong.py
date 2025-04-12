import sys

input_data = sys.stdin.readline

TC = int(input_data().rstrip())

# 음수 가중치가 있고,
# 출발지와 도착지 모두 정해져있지 않으므로
# Floyd-Warshall 쓰면 되지 않을까 생각.

def FloydWarhsall(N, graph):
    for i in range(1, N + 1):
        graph[i][i] = 0
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

# def BellmanFord(N, start, graph, distance):
#     distance[start] = 0
#     minusCycle = False
    
#     for i in range(N):
#         for g in graph[i]:
#             next_pos, next_dist = g
#             dist = distance[i] + next_dist
#             if dist < distance[next_pos]:
#                 distance[next_pos] = dist
#                 if i == N - 1: # (N - 1)번째에도 발생하면 음수 사이클이 있다고 판단
#                     minusCycle = True
                    
#         return distance if not minusCycle else None

for _ in range(TC):
    N, M, W = map(int, input_data().rstrip().split())
    # graph = {}
    INF = float('inf')
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        S, E, T = map(int, input_data().rstrip().split())
        if T < graph[S][E]:
            graph[S][E] = T
            graph[E][S] = T
    for _ in range(W):
        S, E, T = map(int, input_data().rstrip().split())
        if (-T) < graph[S][E]:
            graph[S][E] = (-T)
            
    graph = FloydWarhsall(N, graph)
    result = False
    for i in range(N + 1):
        for j in range(N + 1):
            if i != j:
                total_time = graph[i][j] + graph[j][i]
                if total_time < 0:
                    result = True
                    break
    if result:
        print("YES")
    else:
        print("NO")
    