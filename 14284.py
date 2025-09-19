import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

graph = defaultdict(list)

# 문제 말이 이래저래 하는데
# 결과적으로 그냥 다익스트라 구하는 거 아님?

for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    
s, t = map(int, input().rstrip().split())
    
INF = float('inf')

distances = [INF] * (n + 1)
distances[s] = 0

q = [(0, s)]

while q:
    cd, cn = heapq.heappop(q)
    
    if cd > distances[cn]:
        continue
    
    for nd, nn in graph[cn]:
        distance = cd + nd
        if distance < distances[nn]:
            distances[nn] = distance
            heapq.heappush(q, (distance, nn))
            
print(distances[t])