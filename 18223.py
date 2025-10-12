import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

V, E, P = map(int, input().rstrip().split())

graph = defaultdict(list)

for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    
distances = [float('INF')] * (V + 1)

hq = [(0, 1)]

while hq:
    cd, cn = heapq.heappop(hq)
    if cd >= distances[cn]:
        continue
    distances[cn] = cd
    
    for d, n in graph[cn]:
        nd, nn = cd + d, n
        if nd < distances[nn]:
            heapq.heappush(hq, (nd, nn))
            
distances2 = [float('INF')] * (V + 1)

hq = [(0, P)]

while hq:
    cd, cn = heapq.heappop(hq)
    if cd >= distances2[cn]:
        continue
    distances2[cn] = cd
    
    for d, n in graph[cn]:
        nd, nn = cd + d, n
        if nd < distances2[nn]:
            heapq.heappush(hq, (nd, nn))
            
if distances[V] != float('INF') and distances[P] + distances2[V] == distances[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")