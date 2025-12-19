import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

graph = []
data = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))

data.sort()
# 일단 virus 단계 숫자 낮은 것부터 정렬하여 넣고
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    virus, s, x, y = q.popleft()
    
    if s == target_s:
        break
        
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny)) # 그 다음 timestep에 대한 바이러스를 추가해줌.
                
# 바이러스 단계 낮은 것부터 먼저 퍼진다,
# 라는 거에 대해 막 ideal한 방법을 찾아야하나 했는데
# 그냥 바어리스 단계 순서, 시간 순서대로 차례차례 순서 맞게 queue에 순차적으로 넣어주는 방식으로 처리.

print(graph[target_x - 1][target_y - 1])