import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n, d, c = map(int, input().rstrip().split()) # c가 해킹당한 시작점임

    # 다익스트라

    graph = defaultdict(list)
    
    for _ in range(d):
        a, b, s = map(int, input().rstrip().split())
        graph[b].append((s, a))
        # a -> b 는 아님. 단방향.

    dist = [float('inf')] * (n + 1)
    dist[c] = 0
    
    pq = [(0, c)]

    while pq:
        current_time, current_node = heapq.heappop(pq)

        if dist[current_node] < current_time:
            continue

        for weight, next_node in graph[current_node]:
            new_time = current_time + weight
            if new_time < dist[next_node]:
                dist[next_node] = new_time
                heapq.heappush(pq, (new_time, next_node))

    count = 0
    max_time = 0

    for d in dist:
        if d != float('inf'):
            count += 1
            if d > max_time:
                max_time = d

    print(count, max_time)
