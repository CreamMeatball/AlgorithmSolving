import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

X, Y, Z = map(int, input().split())

def dijkstra(start, skip_node=-1):
    distances = [INF] * (N + 1)
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        if distances[curr_node] < curr_dist:
            continue
            
        for neighbor, weight in graph[curr_node]:
            if neighbor == skip_node:
                continue
                
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                
    return distances

# X -> Y -> Z 경로
dist_X = dijkstra(X)
dist_Y = dijkstra(Y)
path1 = dist_X[Y] + dist_Y[Z] if dist_X[Y] != INF and dist_Y[Z] != INF else -1

# X -> Z 경로
dist_avoid_Y = dijkstra(X, Y)
path2 = dist_avoid_Y[Z] if dist_avoid_Y[Z] != INF else -1

print(path1, path2)