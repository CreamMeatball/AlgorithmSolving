from collections import deque

M = int(input())
grid = []
for _ in range(2):
    grid.append(list(input()))
    
# brute-force 하게 다 찾아야되나 싶은데
# '전체 . 개수' - '최단 경로 . 개수'
# 로 하면 간단히 구할 수 있음!!!
# 왜냐면 어떤 경로를 구했을 때, 나머지 경로 외 부분은 '잉여'가 되는 거고
# 그 '잉여'가 최대화 될 때는, 최단 경로를 구했을 때이기 때문에.

total_white = sum(row.count('.') for row in grid)

queue = deque()
visited = [[False] * M for _ in range(2)]

# 1열(가장 왼쪽)의 하얀색 칸들을 시작점으로 추가
for r in range(2):
    if grid[r][0] == '.':
        queue.append((r, 0, 1))
        visited[r][0] = True

min_path = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while queue:
    r, c, dist = queue.popleft()

    # 가장 오른쪽 열에 도착하면 종료 (BFS이므로 첫 도착이 최단 거리)
    if c == M - 1:
        min_path = dist
        break

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 2 and 0 <= nc < M and not visited[nr][nc] and grid[nr][nc] == '.':
            visited[nr][nc] = True
            queue.append((nr, nc, dist + 1))

# 전체 하얀색 칸 - 최단 경로에 필요한 칸
print(total_white - min_path)