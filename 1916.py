import sys
import heapq

input_data = sys.stdin.readline

N = int(input_data().rstrip())
M = int(input_data().rstrip())

graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v, w = map(int, input_data().rstrip().split())
    graph[u].append((w, v))
        
A, B = map(int, input_data().rstrip().split())

# print(graph)

# for key in graph:
#     graph[key].sort(key=lambda x: x[1])

# print(graph)
    
    
# dijkstra
INF = float('inf')
    
dist = [INF] * (N + 1)
# visited = [False] * (N + 1)

queue = []
dist[A] = 0
heapq.heappush(queue, (dist[A], A))

while queue:
    current_cost, current_pos = heapq.heappop(queue)
    # heap으로 굳이 구현하는 이유는
    # 아래에서 queue에 여러 경로들이 누적되어 append 될텐데
    # queue에 쌓여있는 것들 중, 누적 dist가 가장 짧은 애를 먼저 꺼내서 연산하게 되고
    # 그 연산이 어떠한 N 노드까지의 경로에 대한 최단 dist를 갱신해놨다고 할 때,
    # 이후 queue에서 꺼내진, 다른 경로를 통한 N 노드까지의 경로 탐색 연산을 수행할 때,
    # 앞에서 더 효율적인 최단 dist를 갱신해놨을 경우 굳이 더 연산하지 않아도 되기 때문.
    # 계산량이 줄어들어 더 효율적이기 때문에 heapq 사용.
    
    # 누적된 current_cost는
    # 애초에 최단일 경우일 때의 node를 우선적으로 방문하면서 누적된 값이기에
    # 이전의 어떠한 node를 거치고, 이후 그 때의 node를 다시 탐색하려 시도할 때
    # 이후 탐색에서의 탐색값이 이전에 해당 node를 방문하면서 계산한 최단 dist보다 무조건 크거나 같을 것이므로
    # 아래의 조건문만으로, 굳이 visited(어떤 노드에 도착하여, 해당 노드에서 이어진 모든 경로의 최단값 판별을 해주었다는) 판별을 해주지 않아도 됨.
    # 요약하면 이미 최단경로라고 발탁되어 거친 node를, 또 거치게 되면 어차피 최단 경로임이 아닌 게 분명하므로
    # 누적 거리가 기존의 최단 거리보다 큰 지를 판별하는 것만으로 기존에 최단 경로 상에서 거친 node를 재방문하지 않는 효과를 낳아 visited를 사용하지 않아도 된다.
    if current_cost > dist[current_pos]:
        continue
    
    for neighbor_cost, neighbor_pos in graph[current_pos]:
        sum_cost = current_cost + neighbor_cost
        if sum_cost < dist[neighbor_pos]: # <= 로 하지 않아도 됨
            dist[neighbor_pos] = sum_cost
            # if not visited[neighbor_pos]:
            #     heapq.heappush(queue, (sum_cost, neighbor_pos))
            heapq.heappush(queue, (sum_cost, neighbor_pos))
    # visited[current_pos] = True
            
# 다익스트라는 greedy + dp 같은 느낌            

print(dist[B])
