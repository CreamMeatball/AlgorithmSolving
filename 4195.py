import sys

input_data = sys.stdin.readline

T = int(input_data().rstrip())

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, size, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    
    if root_a == root_b:
        return size[root_a]
    
    # 큰 집합에 작은 집합을 합침
    if size[root_a] < size[root_b]:
        parent[root_a] = root_b
        size[root_b] += size[root_a]
        return size[root_b]
    else:
        parent[root_b] = root_a
        size[root_a] += size[root_b]
        return size[root_a]

for _ in range(T):
    F = int(input_data().rstrip())
    
    parent = {}
    # size 측정하기가 곤란해서(for 돌면서 일일이 추적해서 찾아내 더해줘야함)
    # size 딕셔너리 하나 더 추가한 뒤 union 할 때마다 더해서 size를 저장해주는 방식으로.
    size = {}
    
    for _ in range(F):
        a, b = input_data().rstrip().split()
        
        if a not in parent:
            parent[a] = a
            size[a] = 1
        if b not in parent:
            parent[b] = b
            size[b] = 1
            
        network_size = union(parent, size, a, b)
        # print(f"parent: {parent}")
        # print(f"size: {size}")
        print(network_size)