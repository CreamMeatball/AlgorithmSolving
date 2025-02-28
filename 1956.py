# 시간 초과로 인해 PyPy3로 제출 필

import sys

input_data = sys.stdin.readline

V, E = map(int, input_data().split())

road = [[float('inf') for _ in range(V + 1)] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input_data().split())
    # 플로이드 워셜을 위한
    if c < road[a][b]:
        road[a][b] = c
    
# 플로이드 워셜
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            road[i][j] = min(road[i][j], road[i][k] + road[k][j])
            
# print(road)
            
min_distance = float('inf')
# stopover = range(1, V + 1)

# start, mid, end = 0, 0, 0

# for i in range(1, V + 1):
#     for j in stopover:
#         if i == j:
#             continue
#         if road[i][j] != float('inf') and road[j][i] != float('inf'):
#             distance = road[i][j] + road[j][i]
#             if distance < min_distance:
#                 min_distance = distance
#                 start, mid, end = i, j, i

for i in range(1, V + 1):
    if road[i][i] < min_distance:
        min_distance = road[i][i]
                
if min_distance == float('inf'):
    print(-1)
else:
    print(min_distance)