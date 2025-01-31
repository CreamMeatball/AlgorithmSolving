import sys

input_data = sys.stdin.readline

N, M, R = map(int, input_data().rstrip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input_data().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
    
for i in range(1, N + 1):
    graph[i].sort()
    
visited = [False] * (N + 1)
order = [0] * (N + 1)
depth = 1

def bfs(graph, current_node):
    global visited, depth
    queue = [current_node]
    visited[current_node] = True
    order[current_node] = depth
    while queue:
        current_node = queue.pop(0) # 선입선출
        for next_node in graph[current_node]:
            if not visited[next_node]:
                depth += 1
                queue.append(next_node)
                # 이 때 queue에 추가된 next_node는, while 반복문 상에서 추후에 진행될 예정임.
                # 당장은 graph[current_node] 내의 다음 node에 대해 진행함.
                # 그렇기에 bfs.
                visited[next_node] = True
                order[next_node] = depth
bfs(graph, R)
print('\n'.join(map(str, order[1:])))