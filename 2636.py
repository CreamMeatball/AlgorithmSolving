import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_outer_air():
    visited = [[False] * C for _ in range(R)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif board[nx][ny] == 1:
                    visited[nx][ny] = True

    return visited

time = 0
last_cheese = 0
cheese_count = sum(row.count(1) for row in board)

while True:
    if cheese_count == 0:
        print(time)
        print(last_cheese)
        break
    last_cheese = cheese_count

    visited = get_outer_air()

    to_melt = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == 1:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] and board[ni][nj] == 0:
                        to_melt.append((i, j))
                        break

    for i, j in to_melt:
        board[i][j] = 0
        cheese_count -= 1

    time += 1
