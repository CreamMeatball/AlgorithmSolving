import sys

input_data = sys.stdin.readline

N, M, R = map(int, input_data().rstrip().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input_data().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N + 1):
    graph[i].sort(reverse=True)

order = [0] * (N + 1)
depth = 1

def bfs(graph, current_node):
    global visited, depth
    queue = [current_node]
    visited[current_node] = True
    order[current_node] = depth
    while queue:
        current_node = queue.pop(0)
        for next_node in graph[current_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                depth += 1
                order[next_node] = depth
                
bfs(graph, R)
print("\n".join(map(str, order[1:])))