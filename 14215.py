edge = list(map(int, input().split()))

max_edge_index = edge.index(max(edge))

while(edge[max_edge_index] >= sum(edge) - edge[max_edge_index]):
    edge[max_edge_index] -= 1

print(sum(edge))