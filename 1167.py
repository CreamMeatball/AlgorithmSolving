import sys

sys.setrecursionlimit(10**8)

input_data = sys.stdin.readline

V = int(input_data().rstrip())

graph = {}
for _ in range(V):
    data = list(input_data().rstrip().split())[:-1]
    u = int(data[0])
    connected_nodes = data[1:]
    for i in range(0, len(connected_nodes), 2):
        v = int(connected_nodes[i])
        w = int(connected_nodes[i + 1])
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add((v, w))
        graph[v].add((u, w))
# print(graph)

# 가장 먼 노드와 그 거리를 찾는 DFS 함수
def dfs(node, distance, visited):
    global max_distance, farthest_node
    visited[node] = True
    
    if distance > max_distance:
        max_distance = distance
        farthest_node = node
    
    for next_node, next_distance in graph[node]:
        if not visited[next_node]:
            dfs(next_node, distance + next_distance, visited)

# 첫 번째 DFS: 임의의 노드(여기서는 1)에서 가장 먼 노드 찾기
max_distance = 0
farthest_node = 1
visited = [False] * (V + 1)
dfs(1, 0, visited)

# 두 번째 DFS: 첫 번째에서 찾은 가장 먼 노드에서 다시 가장 먼 노드 찾기
max_distance = 0
visited = [False] * (V + 1)
dfs(farthest_node, 0, visited)

print(max_distance)