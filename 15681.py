import sys
sys.setrecursionlimit(10 ** 8)

input_data = sys.stdin.readline

N, R, Q = map(int, input_data().split())

graph = {}

for _ in range(N - 1):
    u, v = map(int, input_data().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
    
dp = [0] * (N + 1)
visited = [False] * (N + 1)

def dfs(node):
    visited[node] = True
    dp[node] = 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
            dp[node] += dp[neighbor]
            
dfs(R)

for _ in range(Q):
    q = int(input_data())
    print(dp[q])