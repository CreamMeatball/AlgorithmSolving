import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

candies = []
max_x = 0
max_y = 0

for _ in range(N):
    x, y = map(int, input().rstrip().split())
    max_x = max(max_x, x)
    max_y = max(max_y, y)
    candies.append((x, y))

candies_pos = [[False] * (max_y + 1) for _ in range(max_x + 1)]
for x, y in candies:
    candies_pos[x][y] = True

visited = [[-1] * (max_y + 1) for _ in range(max_x + 1)]

directions = [(1, 0), (0, 1)] # 오른쪽, 위쪽

q = deque([(0, 0)])
visited[0][0] = 0

while q:
    cx, cy = q.popleft()
    
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy

        if (nx < 0) or (nx > max_x) or (ny < 0) or (ny > max_y):
            continue

        current_candy = 0
        if candies_pos[nx][ny]:
            current_candy = max(0, int(M - (nx + ny)))

        if visited[nx][ny] < visited[cx][cy] + current_candy:
            visited[nx][ny] = visited[cx][cy] + current_candy
            q.append((nx, ny))

result = 0
for row in visited:
    result = max(result, max(row))
print(result)