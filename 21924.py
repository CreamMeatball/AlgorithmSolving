import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = defaultdict(set)
all_cost = 0

for _ in range(M):
    a, b, cost = map(int, input().rstrip().split())
    graph[a].add((cost, b))
    graph[b].add((cost, a))
    all_cost += cost
    
# Prim (MST)
# Prim 시간복잡도: O(N^2) 또는 heapq 사용 시 O(NlogE) (N: 노드, E: 간선)
# ㄴ heapq 쓰면 (N = E)인 비밀집 그래프에서도 Kruskal이랑 시간 똑같음
# Prim 구현: 우선순위큐 - Greedy

visited = [False] * (N + 1)
total_weight = 0
connected_node = 0
min_heap = [(0, 1)] # (가중치, 현재노드)

while min_heap:
    cw, cn = heapq.heappop(min_heap)
    
    # 아래에서 visited 필터링을 할 것이지만,
    # queue 특성 상 추가될 때 당시엔 not visited였지만 pop되는 시점에는 이미 앞서서 방문해버린 node일 수 있기 때문에,
    # 여기서 다시 한 번 visited 필터링 해줘야 함.
    if visited[cn]:
        continue
    
    total_weight += cw
    connected_node += 1
    visited[cn] = True
    
    for nw, nn in graph[cn]:
        if not visited[nn]:
            heapq.heappush(min_heap, (nw, nn))

# print(all_cost)            
# print(total_weight)            
# print(connected_node)            
            
if connected_node == N:
    print(all_cost - total_weight)
else:
    print(-1)