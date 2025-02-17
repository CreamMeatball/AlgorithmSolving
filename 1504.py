import sys
import heapq

input_data = sys.stdin.readline
testPrint = False
max_size = 200000 * 1000

N, E = map(int, input_data().split())

graph = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, cost = map(int, input_data().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))
    
essential_node = list(map(int, input_data().split()))

# v2를 시작점으로 N으로 가는 다익스트라 최단을 구하고
# v1을 시작점으로 N으로 가는 다익스트라 최단을 구함.
# 1) 1 -> v1 -> v2 -> N
# 2) 1 -> v2 -> v1 -> N
# 위 두 개가 있을 거고,
# 두 개 중 최소값을 출력하면 됨.
# 1)의 경우엔 1 -> v1 로 가는 다익스트라 최단.
# 2)의 경우엔 1 -> v2 로 가는 다익스트라 최단.

def dijkstra(graph, start, end):
    print(f"start dijkstra. start: {start}, end: {end}") if testPrint else None
    distance = [max_size] * (N + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    if distance[end] == max_size:
        return -1
    return distance[end]

# v2 -> N 다익스트라
v2_to_N = dijkstra(graph, essential_node[1], N)
print(f"v2_to_N: {v2_to_N}") if testPrint else None

# v1 -> N 다익스트라
v1_to_N = dijkstra(graph, essential_node[0], N)
print(f"v1_to_N: {v1_to_N}") if testPrint else None

# 1) 1 -> v1 -> v2 -> N
# 1 -> v1 다익스트라
one_to_v1 = dijkstra(graph, 1, essential_node[0])
print(f"one_to_v1: {one_to_v1}") if testPrint else None
# v1 -> v2 다익스트라
v1_to_v2 = dijkstra(graph, essential_node[0], essential_node[1])
print(f"v1_to_v2: {v1_to_v2}") if testPrint else None
# v2 -> N 다익스트라
v2_to_N = dijkstra(graph, essential_node[1], N)
print(f"v2_to_N: {v2_to_N}") if testPrint else None

if (one_to_v1 == -1) or (v1_to_v2 == -1) or (v2_to_N == -1):
    result1 = -1
else:
    result1 = one_to_v1 + v1_to_v2 + v2_to_N
print(f"result1: {result1}") if testPrint else None

# 2) 1 -> v2 -> v1 -> N
# 1 -> v2 다익스트라
one_to_v2 = dijkstra(graph, 1, essential_node[1])
print(f"one_to_v2: {one_to_v2}") if testPrint else None
# v2 -> v1 다익스트라
v2_to_v1 = dijkstra(graph, essential_node[1], essential_node[0])
print(f"v2_to_v1: {v2_to_v1}") if testPrint else None
# v1 -> N 다익스트라
v1_to_N = dijkstra(graph, essential_node[0], N)
print(f"v1_to_N: {v1_to_N}") if testPrint else None

if (one_to_v2 == -1) or (v2_to_v1 == -1) or (v1_to_N == -1):
    result2 = -1
else:
    result2 = one_to_v2 + v2_to_v1 + v1_to_N
print(f"result2: {result2}") if testPrint else None

if result1 == -1 and result2 == -1:
    print(-1)
elif result1 == -1:
    print(result2)
elif result2 == -1:
    print(result1)
else:
    print(min(result1, result2))