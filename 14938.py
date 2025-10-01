import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n, m, r = map(int, input().rstrip().split())

items = [-1] + list(map(int, input().rstrip().split()))

graph = defaultdict(list)

for _ in range(r):
    a, b, l = map(int, input().rstrip().split())
    graph[a].append((l, b))
    graph[b].append((l, a))

items_sum_max = 0

for start in range(1, n + 1):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0

    hq = []
    heapq.heappush(hq, (0, start))
    
    while hq:
        cd, cn = heapq.heappop(hq)
        if cd > distances[cn]:
            continue
        distances[cn] = cd
        for d, nn in graph[cn]:
            nd = cd + d
            if nd < distances[nn]:
                heapq.heappush(hq, (nd, nn))
    
    items_sum = 0
    for i in range(1, n + 1):
        if distances[i] <= m:
            items_sum += items[i]
    # print(f"for start {start}, items_sum: {items_sum}") 
    # print(f"[start: {start}] distances: ")       
    # print(distances[1:])
    items_sum_max = max(items_sum_max, items_sum)
    
print(items_sum_max)