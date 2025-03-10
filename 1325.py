# PyPy3로 제출(시간 초과 발생해서)

import sys
from collections import deque
# sys.setrecursionlimit(10**7)
input_data = sys.stdin.readline

N, M = map(int, input_data().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input_data().split())
    graph[b].append(a)

# def dfs(start):
#     stack = [start]
#     visited[start] = True
#     count = 1
#     while stack:
#         cur = stack.pop()
#         for nxt in graph[cur]:
#             if not visited[nxt]:
#                 visited[nxt] = True
#                 count += 1
#                 stack.append(nxt)
#     return count

# howMany = [0] * (N + 1)
# max_num = 0

# for i in range(1, N + 1):
#     visited = [False]*(N+1)
#     howMany[i] = dfs(i)
#     if howMany[i] > max_num:
#         max_num = howMany[i]

# for i in range(1, N + 1):
#     if howMany[i] == max_num:
#         print(i, end=' ')

def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    count = 1
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
                count += 1
    return count

max_count = 0
result = []
for i in range(1, N + 1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)

# for r in result:
#     print(r, end=' ')
print(*result)