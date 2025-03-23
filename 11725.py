import sys

sys.setrecursionlimit(10**8)

# 루트가 없는 트리: 모든 노드 간에 위계가 없음. 상호 연결만 되어있는 것.
# ㄴ 루트가 없는 트리에서 루트를 정하면, 모든 노드의 위계가 생김(일반적으로 아는 트리)

input_data = sys.stdin.readline

N = int(input_data().rstrip())

graph = {}
for i in range(N - 1):
    a, b = map(int, input_data().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (N + 1)
parent = [-1] * (N + 1)

def dfs(n):
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            parent[i] = n
            dfs(i)
dfs(1)

for i in range(2, N + 1):
    print(parent[i])