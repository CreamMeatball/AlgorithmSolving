import sys
from itertools import combinations
import math
sys.setrecursionlimit(10**5)

input_data = sys.stdin.readline

n = int(input_data().rstrip())

stars_parents = [i for i in range(n + 1)]
stars = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    stars[i] = tuple([i] + list(map(float, input_data().rstrip().split())))
    # ex. stars[3] = (3, 1.0, 2.0)
    
# 1 <= n <= 100 이라 모든 edges 다 구해놓아도 될 듯 (n * (n - 1))   

def cal_dis(a, b):
    a_x, a_y = a
    b_x, b_y = b
    distance = math.sqrt(abs((a_x - b_x)) ** 2 + abs((a_y - b_y)) ** 2)
    return distance

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)
    if root_a < root_b:
        parent[root_b] = parent[root_a]
    else:
        parent[root_a] = parent[root_b]
        
        
edges = []
stars_coupled = combinations(stars[1:], 2)
for sc in stars_coupled:
    a, b = sc
    a_index, a_x, a_y = a
    b_index, b_x, b_y = b
    distance = cal_dis((a_x, a_y), (b_x, b_y))
    edges.append((distance, a_index, b_index))
    
edges.sort(key = lambda x: x[0])
cost = 0.

for e in edges:
    c, a, b = e
    if find(stars_parents, a) != find(stars_parents, b):
        cost += c
        union(stars_parents, a, b)
        
# print(round(cost, 2))
print(cost)