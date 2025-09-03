import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

sex = [0] + list(str(input().rstrip()).split())

# print(sex)

graph = defaultdict(set)

for _ in range(M):
    u, v, d = map(int, input().rstrip().split())
    graph[u].add((d, v))
    graph[v].add((d, u))
    
visited = [False] * (N + 1)
total_weight = 0
count_nodes = 0
min_heap = [(0, 1)] # (현재가중치, 현재노드)

while min_heap:
    cw, cn = heapq.heappop(min_heap)
    
    if visited[cn]:
        continue
    
    cs = sex[cn]
    total_weight += cw
    count_nodes += 1
    visited[cn] = True
    
    for nw, nn in graph[cn]:
        if visited[nn]:
            continue
        ns = sex[nn]
        if cs != ns:
            # print(f"sex[{cn}]({cs}) != sex[{nn}]({ns})")
            heapq.heappush(min_heap, (nw, nn))

if count_nodes == N:
    print(total_weight)
else:
    print(-1)