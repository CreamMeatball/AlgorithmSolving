import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input().rstrip())
K = int(input().rstrip())
a_houses = list(map(int, input().split()))
b_houses = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

# 문제에 총깡총깡 짝폴짝폴, 둘 중에 어쩌구 이런 거 많은데,
# 그냥 결국에 A형 집들과 B형 집들 중에서 최단 거리가 가장 짧은 집 찾으면 됨.

dist = [float('inf')] * (N + 1)
dist[J] = 0
pq = [(0, J)]

while pq:
    current_dist, u = heapq.heappop(pq)
    
    if current_dist > dist[u]:
        continue
        
    for v, weight in graph[u]:
        if dist[v] > current_dist + weight:
            dist[v] = current_dist + weight
            heapq.heappush(pq, (dist[v], v))

min_a = min(dist[h] for h in a_houses)
min_b = min(dist[h] for h in b_houses)

if min_a == float('inf') and min_b == float('inf'):
    print("-1")
elif min_a <= min_b:
    print("A")
    print(min_a)
else:
    print("B")
    print(min_b)
