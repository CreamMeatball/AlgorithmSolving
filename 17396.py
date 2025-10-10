import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
visible = list(map(int, input().rstrip().split()))

graph = defaultdict(list)
for _ in range(M):
    a, b, t = map(int, input().rstrip().split())
    graph[a].append((t, b))
    graph[b].append((t, a))

distances = [float('inf')] * N
hq = [(0, 0)]

while hq:
    cc, cn = heapq.heappop(hq)
    if distances[cn] <= cc:
        continue
    distances[cn] = cc

    for c, n in graph[cn]:
        if n != N - 1 and visible[n] == 1:
            continue

        nc = cc + c
        if nc < distances[n]:
            heapq.heappush(hq, (nc, n))

print(distances[N - 1] if distances[N - 1] != float('inf') else -1)
