import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N = int(input().rstrip())

graph = defaultdict(set)

for i in range(1, N + 1):
    data = [0] + list(map(int, input().rstrip().split()))
    for j in range(1, N + 1):
        weight = data[j]
        graph[i].add((weight, j))
        
# print(graph)

# Prim (MST)
# Prim 시간복잡도: O(N^2) 또는 heapq 사용 시 O(NlogE) (N: 노드, E: 간선)
# ㄴ heapq 쓰면 (N = E)인 비밀집 그래프에서도 Kruskal이랑 시간 똑같음
# Prim 구현: 우선순위큐 - Greedy

visited = [False] * (N + 1)
total_weight = 0
min_heap = [(0, 1)] # (가중치, 현재노드)

while min_heap:
    cw, cn = heapq.heappop(min_heap) # heapq.heappop 을 하기 때문에, 사전에 가중치 오름차순 정렬 해놓을 필요가 없음.
    # 아래에서 visited 필터링 했지만,
    # queue 특성 상 추가될 때 당시엔 not visited였지만 pop되는 시점에는 이미 앞서서 방문해버린 node일 수 있기 때문에,
    # 여기서 다시 한 번 visited 필터링 해줘야 함.
    if visited[cn]:
        continue
    
    visited[cn] = True
    total_weight += cw
    
    for nw, nn in graph[cn]:
        if visited[nn]: # 효율성을 위해 여기서 미리 visited 필터링
            continue
        heapq.heappush(min_heap,(nw, nn))
        
print(total_weight)