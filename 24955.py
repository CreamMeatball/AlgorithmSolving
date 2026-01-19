from collections import deque
import sys
input = sys.stdin.readline

MOD = 1_000_000_007 # 1000000007 과 동일

N, Q = map(int, input().rstrip().split())
A = [0] + list(map(int, input().rstrip().split()))

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 숫자의 자릿수 미리 계산
digit_len = [0] * (N + 1)
for i in range(1, N + 1):
    digit_len[i] = len(str(A[i]))

# BFS로 x -> y 경로 찾기
def bfs(start, end):
    parent = [-1] * (N + 1)
    q = deque([start])
    parent[start] = start

    while q:
        cur = q.popleft()
        if cur == end:
            break
        for nxt in graph[cur]:
            if parent[nxt] == -1:
                parent[nxt] = cur
                q.append(nxt)

    # 경로 복원
    path = []
    cur = end
    while True:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]
    path.reverse()
    return path

for _ in range(Q):
    x, y = map(int, input().split())
    path = bfs(x, y)

    result = 0
    for node in path:
        result = (result * pow(10, digit_len[node], MOD) + A[node]) % MOD

    print(result)