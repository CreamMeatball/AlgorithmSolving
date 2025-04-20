import sys
from collections import deque

input_data = sys.stdin.readline

def is_tree(graph, start, visited): # dfs
    node_count = 0
    edge_count = 0
    
    queue = deque([start])
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        node_count += 1
        
        for neighbor in graph[node]:
            edge_count += 1
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    # 무방향 간선을 양쪽에서 모두 탐색하므로, 각 간선은 양쪽에서 각각 한 번씩 세어지므로 2로 나눔
    edge_count //= 2
    
    # 트리임을 판단(사이클일 경우 트리X): 트리는 간선 수 = 노드 수 - 1 이어야 함
    return edge_count == node_count - 1

index = 1

while True:
    n, m = map(int, input_data().rstrip().split())
    if n == 0 and m == 0:
        break

    nodes = []
    graph = {}
    for i in range(1, n + 1):
        nodes.append(i)
        graph[i] = []
    
    for i in range(m):
        a, b = map(int, input_data().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
        
    visited = [False] * (n + 1)
    tree_count = 0
    
    for i in range(1, n + 1):
        if not visited[i]:
            if is_tree(graph, i, visited):
                tree_count += 1
    
    if tree_count == 0:
        print(f"Case {index}: No trees.")
    elif tree_count == 1:
        print(f"Case {index}: There is one tree.")
    else:
        print(f"Case {index}: A forest of {tree_count} trees.")
    
    index += 1
    continue