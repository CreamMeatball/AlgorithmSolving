import sys
from collections import deque

input_ = sys.stdin.readline

N, M, K = map(int, input_().split())
    
map_ = []
map_.append([-1] * (M + 2))
for _ in range(N):
    map_.append([-1] + [0] * (M) + [-1])
map_.append([-1] * (M + 2))

for _ in range(K):
    r, c = map(int, input_().split())
    map_[r][c] = 1
    
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * (M + 2) for _ in range(N + 2)]

def bfs(map_, start):
    x, y = start
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    
    while queue:
        x, y = queue.popleft()
        for d in directions:
            next_x, next_y = x + d[0], y + d[1]
            if not visited[next_x][next_y] and map_[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                count += 1
                queue.append((next_x, next_y))
                
    return count
    
max_count = 0   
    
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if not visited[i][j] and map_[i][j] == 1:
            count = bfs(map_, (i, j))
            if count > max_count: max_count = count
            
print(max_count)