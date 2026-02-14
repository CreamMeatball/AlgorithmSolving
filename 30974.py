# PyPy3

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = float('inf')

# 에라토스테네스의 체 (최대 합 10,000,000)
MAX_VAL = 10000000
is_prime = [True] * (MAX_VAL + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX_VAL**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX_VAL + 1, i):
            is_prime[j] = False

n, m = map(int, input().split())
codes = list(map(int, input().split()))

# 그래프 구성. 합이 소수인 경우만 연결
adj = defaultdict(list)
for _ in range(m):
    u, v, w = map(int, input().split())
    if is_prime[codes[u-1] + codes[v-1]]:
        adj[u].append((v, w))
        adj[v].append((u, w))

# 다익스트라
distances = [INF] * (n + 1)
distances[1] = 0
pq = [(0, 1)]

while pq:
    dist, current = heapq.heappop(pq)
    
    if distances[current] < dist:
        continue
        
    for next_node, weight in adj[current]:
        cost = dist + weight
        if cost < distances[next_node]:
            distances[next_node] = cost
            heapq.heappush(pq, (cost, next_node))

if distances[n] == INF:
    print("Now where are you?")
else:
    print(distances[n])