import sys
sys.setrecursionlimit(10**5)

input_data = sys.stdin.readline

n, m = map(int, input_data().rstrip().split())

group = list(i for i in range(n + 1))
# print(group)

def find_parent(group, x):
    if group[x] != x:
    #     return find_parent(group, group[x])
        group[x] = find_parent(group, group[x])
        # 이렇게 하면 tracking 하면서 지나는 모든 경로의 값들의 parent를 루트 노드로 설정하게 되어서 더 시간 효율적임
    # return x
    
    # 기존 방식은 경로 상의 값들을 변경해주지 않고
    # 최종 root node가 무엇인지만 반환
    return group[x]

def union(group, a, b):
    # a의 root node 찾기
    root_node_a = find_parent(group, a)
    # b의 root node 찾기
    root_node_b = find_parent(group, b)
    
    if root_node_a < root_node_b:
        group[root_node_b] = root_node_a
    else:
        group[root_node_a] = root_node_b

for _ in range(m):
    type, a, b = map(int, input_data().rstrip().split())
    if type == 0:
        union(group, a, b)
    elif type == 1:
        if find_parent(group, a) == find_parent(group, b):
            print("YES")
        else:
            print("NO")