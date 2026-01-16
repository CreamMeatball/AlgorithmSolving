# PyPy3 for avoiding time exceed

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M, X, Y = map(int, input().rstrip().split())

graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 그냥 직관적으로 단순하게
# 모든 연결된 정점에 대해, 연결된 정점(이웃)과 이동 횟수 정보를 큐에 넣고
# 큐에서 꺼냈을 떄 이동 횟수가 Y면, 정답 리스트에 정점 정보를 넣는다.
    
# visited[node][count]: node에 cnt번 이동해서 도착했는지 여부
visited = [[False] * (Y + 1) for _ in range(N + 1)]
queue = deque([(X, 0)])
visited[X][0] = True

possible_nodes = set()

while queue:
    curr, count = queue.popleft()

    if count == Y:
        possible_nodes.add(curr)
        continue
    
    for neighbor in graph[curr]:
        if not visited[neighbor][count + 1]:
            visited[neighbor][count + 1] = True
            queue.append((neighbor, count + 1))

if not possible_nodes:
    print(-1)
else:
    print(*sorted(list(possible_nodes)))