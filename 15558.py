from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
board = [list(input().rstrip()), list(input().rstrip())]

visited = [[False] * N for _ in range(2)]

q = deque()
q.append((0, 0, 0))  # (row, col, time)
visited[0][0] = True

while q:
    row, col, time = q.popleft()
    next_time = time + 1

    # 앞으로
    nc = col + 1
    if nc >= N:
        print(1)
        break
    if nc > time and board[row][nc] == '1' and not visited[row][nc]:
        visited[row][nc] = True
        q.append((row, nc, next_time))

    # 뒤로
    nc = col - 1
    if nc > time and nc >= 0 and board[row][nc] == '1' and not visited[row][nc]:
        visited[row][nc] = True
        q.append((row, nc, next_time))

    # 점프
    nr = 1 - row
    nc = col + K
    if nc >= N:
        print(1)
        break
    if nc > time and board[nr][nc] == '1' and not visited[nr][nc]:
        visited[nr][nc] = True
        q.append((nr, nc, next_time))
else:
    print(0)