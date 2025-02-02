import sys

input_data =  sys.stdin.readline

N = int(input_data().rstrip())
M = int(input_data().rstrip())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input_data().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(graph, current_node):
    global visited, count
    queue = [current_node]
    visited[current_node] = True
    # count += 1
    while queue:
        current_node = queue.pop(0)
        for next_node in graph[current_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                count += 1
                
bfs(graph, 1)
print(count)