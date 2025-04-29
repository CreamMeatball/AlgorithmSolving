import sys

# '가장 적은 종류의 비행기'를 타는 게 목표
# -> MST를 뜻함
# MST: Spanning Tree 중에서 사용된 간선들의 가중치 합이 최소인 트리
# Spanning Tree: 그래프 내의 모든 정점을 포함하는 Tree
# Tree: 노드들의 집합으로 구성되며, 하나의 루트 노드를 기준으로 계층적(parent-child) 관계를 가지는 구조로,
#   사이클이 없는 연결 그래프(acyclic connected graph)

# MST 구현 알고리즘:
# 1. Kruskal (Greedy)
# 2. Prim

input_data = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_node_a = find(parent, a)
    root_node_b = find(parent, b)
    if root_node_a < root_node_b:
        parent[root_node_b] = root_node_a
    else:
        parent[root_node_a] = root_node_b

T = int(input_data().rstrip())
for _ in range(T):
    N, M = map(int, input_data().rstrip().split())
    edges = []
    for _ in range(M):
        a, b = map(int, input_data().rstrip().split())
        edges.append([a, b])
        
    parents = [i for i in range(N + 1)]
    
    count = 0
    for e in edges:
        a, b = e
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            count += 1
            
    print(count)