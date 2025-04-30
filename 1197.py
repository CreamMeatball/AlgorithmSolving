import sys

# Kruskal 알고리즘 -> 무방향 그래프일 때 사용 가능 + 가중치 양수/음수 상관 없음

sys.setrecursionlimit(10 ** 5)
input_data = sys.stdin.readline

V, E = map(int, input_data().rstrip().split())
edges = []
for _ in range(E):
    A, B, C = map(int, input_data().rstrip().split())
    edges.append((C, A, B))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b
        
edges.sort(key=lambda x: x[0])

parents = [i for i in range(V + 1)]
costs = 0

for e in edges:
    c, a, b = e
    if find(parents, a) != find(parents, b):
        union(parents, a, b)
        costs += c
        
print(costs)