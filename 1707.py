# 방법론:
# 인접한 노드끼리 서로 다른 색깔을 가지고 있으면 이분 그래프가 됨.
# 간선을 타고 다음 node로 건너갈 때마다 색깔이 달라지면 됨.
# 만약 다음 node로 건너가야 하는데, 지금 node의 color와 다음 node의 color가 같게 될 경우 False 반환.

import sys

sys.setrecursionlimit(10**7)

input_data = sys.stdin.readline

testPrint = False
K = int(input_data())

def dfs(graph, v, visited, color_list, color):
    visited[v] = True
    color_list[v] = color
    print(f"color_list: {color_list[1:]}") if testPrint else None
    for nxt in graph[v]:
        if not visited[nxt]:
            print(f"current node: {v}, color: {color}, nxt node: {nxt}, color_list: {color_list[1:]}") if testPrint else None
            if not dfs(graph, nxt, visited, color_list, -color):
                return False
        elif (color_list[nxt] != 0) and (color_list[nxt] == color):
            print(f"color conflict. \n current_node's color == nxt node's color. \n current node: {v}, color: {color}, nxt_node: {nxt}, color_list: {color_list[1:]}") if testPrint else None
            return False
    return True

for _ in range(K):
    V, E = map(int, input_data().split())
    graph = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        u, v = map(int, input_data().split())
        graph[u].append(v)
        graph[v].append(u)
    
    if testPrint:
        for i in range(1, V + 1):
            print(f"{i}'s graph: {graph[i]}")
    
    # 연결 요소마다 한 번씩만 방문 체크를 위해 visited와 color_list를 전역으로 관리
    visited = [False] * (V + 1)
    color_list = [0] * (V + 1)
    
    isBipartite = True
    for v in range(1, V + 1):
        print(f"-- v: {v} --") if testPrint else None
        if not visited[v]:
            # 아직 색깔이 정해지지 않은 정점은 임의의 색(예: 1)으로 시작
            if not dfs(graph, v, visited, color_list, 1):
                isBipartite = False
                break
    
    print("YES" if isBipartite else "NO")