import sys
sys.setrecursionlimit(10**7) # 재귀 제한 늘리기 (안하면 RecursionError 발생). BOJ에서 기본값이 1000으로 되어있음.

input_data = sys.stdin.readline

testPrint = False

N, M, R = map(int, input_data().rstrip().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input_data().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
    
print(graph) if testPrint else None

for i in range(1, N + 1):
    graph[i].sort()
    
print(graph) if testPrint else None

def dfs(graph, v, visited, order, depth):
    visited[v] = True
    order[v] = depth[0]  # v번 정점의 방문 순서 기록
    for nxt in graph[v]:
        if not visited[nxt]:
            depth[0] += 1
            dfs(graph, nxt, visited, order, depth)

visited = [False] * (N + 1)
order = [0] * (N + 1)
depth = [1]

dfs(graph, R, visited, order, depth)

for i in range(1, N + 1):
    print(order[i])