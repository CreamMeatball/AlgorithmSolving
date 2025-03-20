import sys
from collections import deque
import heapq

input_data = sys.stdin.readline

n = int(input_data().rstrip())
m = int(input_data().rstrip())

# 간선 cost가 있어서 MST(최소신장트리) 써야할 듯
# Prim 알고리즘 써야할 듯

bus = {}
for _ in range(m):
    data = list(map(int, input_data().rstrip().split()))
    start, end, cost = data[0], data[1], data[2]
    if start not in bus:
        bus[start] = []
    bus[start].append((end, cost))

start, end = map(int, input_data().rstrip().split())

def prim(start, end):
    heap = []
    included = [False] * (n + 1)
    sum_cost = 0
    current = start
    heapq.heappush(heap, (0, start))
    
    while heap:
        cost, current = heapq.heappop(heap)
        if included[current]:
            continue
        included[current] = True
        sum_cost += cost
        if current == end:
            return sum_cost
        
        if current in bus:
            for next, cost in bus[current]:
                if not included[next]:
                    heapq.heappush(heap, (cost, next))
    return sum_cost

print(prim(start, end))