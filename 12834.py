import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, V, E = map(int, input().split())
A, B = map(int, input().split())

homes = list(map(int, input().split()))

graph = defaultdict(list)

for _ in range(E):
    a, b, l = map(int, input().split())
    graph[a].append((l, b))
    graph[b].append((l, a))
    
# 각 사람들의 수만큼 A와 B까지의 거리를 계산하는 걸 반복하는 게 아니라 (N번 반복이 아니라)
# A와 B를 도착점이 아닌 출발점으로 하여 2번만 계산한 뒤에
# 그 계산한 dist 테이블을 가지고 (freeze) N명의 사람들 각각에 대해 단순 계산

def get_dists(start):
    dists = [float('inf')] * (V + 1)
    dists[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, curr = heapq.heappop(pq)
        if dists[curr] < d: continue
        for weight, nxt in graph[curr]:
            if dists[nxt] > d + weight:
                dists[nxt] = d + weight
                heapq.heappush(pq, (dists[nxt], nxt))
    return [-1 if x == float('inf') else x for x in dists]

dist_A = get_dists(A)
dist_B = get_dists(B)

# 각 팀원의 (집-A 거리) + (집-B 거리) 합산
total_distance = 0
for h in homes:
    total_distance += dist_A[h] + dist_B[h]

print(total_distance)