import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N, M, X, Y = map(int, input().split())

adj = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

dist = [float('inf')] * N
dist[Y] = 0
hq = [(0, Y)]

while hq:
    d, u = heapq.heappop(hq)
    if d > dist[u]:
        continue
    for v, w in adj[u]:
        if dist[v] > d + w:
            dist[v] = d + w
            heapq.heappush(hq, (dist[v], v))

rounds = []

for i in range(N):
    if i == Y: continue
    if dist[i] == float('inf') or dist[i] * 2 > X:
        print(-1)
        sys.exit()
    rounds.append(dist[i] * 2)

rounds.sort()

days = 0
current_x = 0
for r in rounds:
    if current_x + r <= X:
        current_x += r
    else:
        days += 1
        current_x = r

if current_x > 0:
    days += 1

print(days if rounds else 0)