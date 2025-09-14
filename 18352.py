import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M, K, X = map(int, input().rstrip().split())

graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)
    
# 다익스트라    
# BFS (거리를 기록하고, 가장 먼저 X 거리 노드를 찾은 이후에도 더 탐색하는) 로도 풀 수 있을 듯.
    
INF = float('inf')
distance = [INF] * (N + 1)
distance[X] = 0

queue = []
heapq.heappush(queue, (0, X))

while queue:
    cd, cn = heapq.heappop(queue)
    if cd > distance[cn]:
        continue
    
    for nn in graph[cn]:
        nd = cd + 1
        if nd < distance[nn]:
            distance[nn] = nd
            heapq.heappush(queue, (nd, nn))
            
found = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        found = True

if not found:
    print(-1)