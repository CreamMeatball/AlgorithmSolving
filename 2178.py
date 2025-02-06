import sys
from collections import deque

input_data = sys.stdin.readline
n, m = map(int, input_data().split())
maze = [list(map(int, input_data().rstrip())) for _ in range(n)]
distance = [[0] * m for _ in range(n)]

queue = deque()
queue.append((0, 0))
distance[0][0] = 1

# 상, 하, 좌, 우 이동
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS는 레벨 순서대로(깊이가 얕은 순으로) 노드를 탐색하기 때문에,
# 처음 도착한 노드가 해당 노드까지 도달하는 최단 경로임이 보장됨.
# 굳이 최소인지 아닌지 비교하거나, dp 같은 거 쓸 필요 없이
# 처음 도착하면 값 출력하고 break 해버리면 됨. 그럼 그게 최소값임.
# LEGEND..

while queue:
    r, c = queue.popleft()
    if r == n - 1 and c == m - 1:
        print(distance[r][c])
        break
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m:
            if maze[nr][nc] == 1 and distance[nr][nc] == 0:
                distance[nr][nc] = distance[r][c] + 1
                queue.append((nr, nc))