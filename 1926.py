import sys
from collections import deque
input_ = sys.stdin.readline

n, m = map(int, input_().split())
painting = []
painting.append([-1] * (m + 2))
for _ in range(n):
    painting.append([-1] + list(map(int, input_().split())) + [-1])
painting.append([-1] * (m + 2))
    
count = 0
max_area = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * (m + 2) for _ in range(n + 2)]

def bfs(init, painting):
    global count
    area = 1
    count += 1
    queue = deque()
    queue.append((init[0], init[1]))
    visited[init[0]][init[1]] = True
    
    while queue:
        current = queue.popleft()
        for d in directions:
            next_x = current[0] + d[0]
            next_y = current[1] + d[1]
            if not visited[next_x][next_y] and painting[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                area += 1
                queue.append((next_x, next_y))
                
    return area

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if not visited[i][j] and painting[i][j] == 1:
            area = bfs((i, j), painting)
            if area > max_area:
                max_area = area
                
print(count)
print(max_area)