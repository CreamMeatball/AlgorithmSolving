import sys
from collections import deque

N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N)]
indegree = [0] * N

for _ in range(M):
    a, b = input().rstrip().split()
    u = ord(a) - ord('A')
    v = ord(b) - ord('A')
    graph[u].append(v)
    indegree[v] += 1

# 검거된 공급책
data = input().rstrip().split()
K = int(data[0])
arrested = set(ord(x) - ord('A') for x in data[1:])

# 초기 원산지 찾기 (초기 indegree == 0)
origins = [i for i in range(N) if indegree[i] == 0 and i not in arrested]

# BFS
visited = [False] * N
q = deque()

for o in origins:
    visited[o] = True
    q.append(o)

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if nxt in arrested:
            continue
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)

# 결과 계산 (원산지 제외, 검거된 사람 제외)
answer = 0
for i in range(N):
    if visited[i] and i not in origins and i not in arrested:
        answer += 1

print(answer)
