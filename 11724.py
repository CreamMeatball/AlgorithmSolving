import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(v):
    visited[v] = True
    for neighbor in adj[v]:
        if not visited[neighbor]:
            dfs(neighbor)

count = 0

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
