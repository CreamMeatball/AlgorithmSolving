import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

graphs = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    graphs[a].append((c, b))
    graphs[b].append((c, a))
    
# for g in graphs.items():
#     print(g)

# MST (최소 신장 트리) 구현인데
# Kruskal vs Prim 선택 기준
# Kruskal: 노드 개수랑 간선 개수랑 비슷할 때
# Prim: 노드 개수보다 간선 개수가 훨씬 많을 때 (밀집 그래프)

# 왜냐면 시간 복잡도가 (노드 수: N, 간선 수: E)
# Kruskal: O(ElogE)
# Prim: O(N^2) 또는 heapq 사용 시 O(NlogE)
# (=> 그래서 걍 heapq 사용 Prim 알고리즘 쓰면 되는 듯? N = E 인 그래프에서 heapq 프림 쓰면 크루스칼이랑 시간 복잡도 똑같음)

# 구현
# Kruskal: 간선 가중치 기준 오름차순 정렬 - 유니온 파인드
# Prim: 우선순위큐 - Greedy

visited = [False] * (N + 1)
total_weight = 0
min_heap = [(0, 1)] # 가중치, 현재 정점

while min_heap:
    w, u = heapq.heappop(min_heap)
    if visited[u]:
        continue
    visited[u] = True
    total_weight += w
        
    for weight, v in graphs[u]:
        if not visited[v]:
            heapq.heappush(min_heap, (weight, v))
            
print(total_weight)