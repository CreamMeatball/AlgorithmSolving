import sys

input_data = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def unionNcheck(parent, a, b):
    global count
    root_node_a = find(parent, a)
    root_node_b = find(parent, b)
    
    if root_node_a == root_node_b:
        return True
    elif root_node_a < root_node_b:
        parent[root_node_b] = root_node_a
    else:
        parent[root_node_a] = root_node_b
    return False

n, m = map(int, input_data().rstrip().split())
points = [i for i in range(n)]
for i in range(1, m + 1):
    a, b = map(int, input_data().rstrip().split())
    check = unionNcheck(points, a, b)
    if check:
        print(i)
        break
else: # for-else. for문이 break 되지 않고 다 실행됐을 경우.
    print(0)