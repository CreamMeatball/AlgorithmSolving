import sys

sys.setrecursionlimit(10**5)
input_data = sys.stdin.readline

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

while(True):
    m, n = map(int, input_data().rstrip().split())
    if m == 0 and n == 0:
        break
    roads = []
    init_cost = 0
    cost = 0
    
    for _ in range(n):
        x, y, z = map(int, input_data().rstrip().split())
        init_cost += z
        roads.append((z, x, y))
    
    roads.sort(key=lambda x: x[0])
    
    parents = [i for i in range(m + 1)]
    
    for r in roads:
        z, x, y = r
        if find(parents, x) != find(parents, y):
            union(parents, x, y)
            cost += z
            
    print(init_cost - cost)