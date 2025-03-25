import sys

sys.setrecursionlimit(10**8)

input_data = sys.stdin.readline

n = int(input_data().rstrip())

graph = {}
for _ in range(n - 1):
    data = list(map(int, input_data().split()))
    if len(data) >= 3:
        u, v, w = data[0], data[1], data[2]
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()
        graph[u].add((v, w))
        graph[v].add((u, w)) # 무방향 그래프로 양쪽 모두에게 통로 설정
    else:
        u = data[0]
        if u not in graph:
            graph[u] = set()

# print(f"graph: ")
# print(graph)    

# 루트(1)에서 제일 먼 곳 하나 찾은다음
# 그 먼곳에서 가장 먼 곳 구하기

def dfs(node, distance, visited):
    global max_distance, farthest_node
    visited[node] = True
    
    if distance > max_distance:
        max_distance = distance
        farthest_node = node
    
    # for next_node, next_distance in graph[node]:
    for next_node, next_distance in graph.get(node, set()):
        if not visited[next_node]:
            dfs(next_node, distance + next_distance, visited)

farthest_node = 1

max_distance = 0
visited = [False] * (n + 1)
dfs(1, 0, visited)

max_distance = 0
visited = [False] * (n + 1)
visited[farthest_node] = True
dfs(farthest_node, 0, visited)

print(max_distance)