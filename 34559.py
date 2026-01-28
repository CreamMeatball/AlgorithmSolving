import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
q = deque()

# 건물(1)로 둘러싸인 0도 건물도 취급한다, 라는 로직은
# BFS로 처리할 경우, 별도 로직으로 처리해주지 않아도 됨
# 탐색 중 건물을 못 뚫는다고 하면, 1로 둘러싸인 내부 0에는 어차피 못들어가기 때문에.

for i in range(N):
    for j in [0, M - 1]:
        if board[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            q.append((i, j))

for j in range(M):
    for i in [0, N - 1]:
        if board[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            q.append((i, j))

# BFS
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


building = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            building[i][j] = 1
        elif board[i][j] == 0 and not visited[i][j]:
            building[i][j] = 1


ps = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        ps[i][j] = (
            building[i - 1][j - 1]
            + ps[i - 1][j]
            + ps[i][j - 1]
            - ps[i - 1][j - 1]
        )

# r1, c1, r2, c2 내 범위를 어쩌구~ 하라 같은 문제의 경우
# 대부분 누적합 쓴다고 생각하면 될 듯
# 그러지 않으면 너무 비효율적으로 계산해야해서.
# 한 번만 탐색해서 누적합 계산해놓고, 그 계산해놓은 거 가지고 이후엔 효율적으로 처리

Q = int(input())

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    # 누적합 계산해놨던 거 이용
    cnt = (
        ps[r2][c2]
        - ps[r1 - 1][c2]
        - ps[r2][c1 - 1]
        + ps[r1 - 1][c1 - 1]
    )
    if cnt == 0:
        print("Yes")
    else:
        print(f"No {cnt}")