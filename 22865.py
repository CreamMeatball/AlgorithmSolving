import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N = int(input().rstrip())

A, B, C = map(int, input().rstrip().split())

M = int(input().rstrip())

graph = defaultdict(list)

for _ in range(M):
    D, E, L = map(int, input().rstrip().split())
    graph[D].append((L, E))
    graph[E].append((L, D))

dist = [float('inf')] * (N + 1)
dist[A] = 0
dist[B] = 0
dist[C] = 0

# A, B, C을 도착점이 아닌 출발점으로 잡자 (다중 출발지 다익스트라)

hq = [(0, A), (0, B), (0, C)]

while hq:
    current_dist, current_node = heapq.heappop(hq)
    for next_dist, next_node in graph[current_node]:
        new_dist = current_dist + next_dist
        if new_dist < dist[next_node]:
            dist[next_node] = new_dist
            heapq.heappush(hq, (new_dist, next_node))

print(dist.index(max(dist[1:])))
