import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = defaultdict(list)

for i in range(M):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
    
distances = [float('inf')] * (N + 1)

hq = [(0, 1)]

while hq:
    cc, cn = heapq.heappop(hq)
    if distances[cn] <= cc: # < 이 아닌 <= 으로 꼭 해야하는 듯. 안 그러면 무한 사이클 생길 수 있는 것 같음(C가 0일 수 있기 때문에)
        continue
    else:
        distances[cn] = cc
    
    for c, n in graph[cn]:
        nc = cc + c
        nn = n
        if nc < distances[nn]:
            heapq.heappush(hq, (nc, nn))
            
print(distances[N])