import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

adj = defaultdict(list)

for _ in range(M):
    S, E, T = map(int, input().split())
    adj[S].append((E, T))
    adj[E].append((S, T))

A, B = map(int, input().split())
dist = [[float('inf')] * 2 for _ in range(N + 1)]
hq = []

for v, T in adj[A]:
    dist[v][T] = 0
    heapq.heappush(hq, (0, v, T))

while hq:
    d, u, t = heapq.heappop(hq)
    
    if d > dist[u][t]:
        continue
    
    for v, nt in adj[u]:
        # 이전 선로(t)와 다음 선로(nt)의 타입이 다르면 절연 발생
        if t != nt:
            cost = d + 1
        else:
            cost = d
            
        if dist[v][nt] > cost:
            dist[v][nt] = cost
            heapq.heappush(hq, (cost, v, nt))

print(min(dist[B]) if A != B else 0)