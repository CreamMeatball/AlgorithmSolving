import sys

input_data = sys.stdin.readline

N = int(input_data().rstrip())
M = int(input_data().rstrip())

cities = [i for i in range(0, N + 1)]
# 0 ~ N 까지 생성, 사용은 1 ~ N

def find(group, x):
    if group[x] != x:
        group[x] = find(group, group[x])
    return group[x]

def union(group, a, b):
    root_node_a = find(group, a)
    root_node_b = find(group, b)
    
    if root_node_a < root_node_b:
        group[root_node_b] = root_node_a
    else:
        group[root_node_a] = root_node_b

for i in range(1, N + 1):
    data = [0] + list(map(int, input_data().rstrip().split()))
    for j, d in enumerate(data):
        if d == 1:
            union(cities, i, j)

result = True
data = list(map(int, input_data().rstrip().split()))
for i in range(0, M - 1):
    a, b = data[i], data[i + 1]
    if find(cities, a) == find(cities, b):
        continue
    else:
        result = False
        break
    
print("YES") if result else print("NO")