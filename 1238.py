import sys
import heapq

input_data = sys.stdin.readline

N, M, X = map(int, input_data().rstrip().split())

# floyd warshall이 시간 초과 나서
# dijkstra * N * 2 번 반복해보기

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input_data().rstrip().split())
    graph[u].append((v, w))        # u -> v 방향
    reverse_graph[v].append((u, w))  # v -> u 방향(역방향)

def dijkstra(start, graph):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        if distance[now] < dist:
            continue
            
        for next_node, next_cost in graph[now]:
            cost = dist + next_cost
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
                
    return distance

# X에서 모든 마을로의 최단거리
to_home = dijkstra(X, graph)

# 모든 마을에서 X로의 최단거리
to_party = dijkstra(X, reverse_graph)

# 각 학생별 왕복 시간 계산 및 최대값 찾기
max_time = 0
for i in range(1, N + 1):
    total_time = to_party[i] + to_home[i]
    max_time = max(max_time, total_time)

print(max_time)