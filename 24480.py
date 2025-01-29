import sys

sys.setrecursionlimit(10**8)
testPrint = False
input_data = sys.stdin.readline

N, M, R = map(int, input_data().rstrip().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input_data().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N + 1):
    graph[i].sort(reverse=True)
print(f"graph: {graph}") if testPrint else None
    
visited = [False] * (N + 1)
order = [0] * (N + 1)
depth = 1

def dfs(graph, current_node):
    global visited, depth
    # depth를 global로 안 받고, parameter 통해서 locality 하게 받으면 문제가 생기는데,
    # 특정 node를 current_node로 dfs가 호출되고 수행되고 나면,
    # 이전 재귀 단계의 dfs()로 돌아가게 되는데, 이 때 depth가 갱신이 안되어있음.
    # 그래서 동일한 depth로 덮어쓰는 문제가 생김.
    print(f"current_node: {current_node}, graph[{current_node}] : {graph[current_node]}, depth: {depth}") if testPrint else None
    visited[current_node] = True
    order[current_node] = depth
    # depth += 1
    print(f"order: {order}") if testPrint else None
    for next_node in graph[current_node]:
        if not visited[next_node]:
            depth += 1
            dfs(graph, next_node)

dfs(graph, R)

print('\n'.join(map(str, order[1:])))