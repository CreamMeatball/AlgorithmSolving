# 간선 가중치가 있는 경우 다익스트라 사용

import sys
# from collections import deque
# deque이 더 빠른데, 메모리가 훨씬 많이 들음.
# deque으로 풀었다가 메모리 초과나서 deque이 아니면서 속도가 빠른 heap 사용.
import heapq

input_data = sys.stdin.readline

V, E = map(int, input_data().split())
S = int(input_data())

graph = [[] for _ in range(V + 1)]

max_cost = 20000 * 10
cost = [max_cost] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input_data().split())
    graph[u].append((v, w))

# 다익스트라.
# bfs 비슷한 느낌임.
def daikstra(start):
    global graph, cost
    queue = []
    cost[start] = 0
    heapq.heappush(queue, (0, start))
    # heapq.heappush(넣을배열, (priority, data)) # 이 부분이 핵심.
    while queue:
        current_cost, current = heapq.heappop(queue)
        if cost[current] < current_cost: # 쓸데없이 반복 안돌게끔
            continue
        for next_node, next_cost in graph[current]:
            new_cost = current_cost + next_cost
            if new_cost < cost[next_node]:
                cost[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))
            
daikstra(S)
for i in range(1, V + 1):
    print(cost[i] if cost[i] != max_cost else "INF")