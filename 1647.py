import sys

input_ = sys.stdin.readline

N, M = map(int, input_().split())

roads = []

for _ in range(M):
    A, B, C = map(int, input_().split())
    roads.append((C, A, B))
    
roads.sort(key=lambda x: x[0])
    
# 하나의 최소 신장 트리로 만든 뒤에
# 남아있는 길 중 하나만 끊으면
# 무조건 두 그룹으로 나눠지는 거 아님?

# 최소 신장 트리 만든 뒤에, 남은 길 중 cost 제일 높은 애 하나 제거하면 되겠네

# Kruskal

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
        
    
parent = [i for i in range(N + 1)]

total_cost = 0
max_cost_road = 0

for c, a, b in roads:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        if c > max_cost_road:
            max_cost_road = c
        total_cost += c 
        
total_cost -= max_cost_road
print(total_cost)