import sys

input_data = sys.stdin.readline

N, M, V = map(int, input_data().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input_data().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
dfs_order = []
bfs_order = []

def dfs(graph, current_node):
    global visited, dfs_order
    visited[current_node] = True
    dfs_order.append(current_node)
    for next_node in graph[current_node]:
        if (next_node) and (not visited[next_node]):
            dfs(graph, next_node)
        else:
            continue
        
def bfs(graph, start_node):
    global visited, bfs_order
    queue = [start_node]
    visited[start_node] = True
    while queue:
        current_node = queue.pop(0)
        bfs_order.append(current_node)
        for next_node in graph[current_node]:
            if (next_node) and (not visited[next_node]):
                queue.append(next_node)
                visited[next_node] = True
            else:
                continue
            
def clearList():
    global visited, dfs_order, bfs_order
    visited = [False] * (N + 1)
    # dfs_order = []
    # bfs_order = []
            
dfs(graph, V)
print(" ".join(map(str, dfs_order)))
clearList()

bfs(graph, V)
print(" ".join(map(str, bfs_order)))
clearList()
