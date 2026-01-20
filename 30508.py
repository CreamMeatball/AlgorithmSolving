from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
h, w = map(int, input().rstrip().split())
H = [list(map(int, input().rstrip().split())) for _ in range(N)]

K = int(input().rstrip())
drain = [[False] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().rstrip().split())
    drain[r-1][c-1] = True

# BFS로 물이 빠지는 칸 계산
# 첫 위치부터 마지막 위치까지 brute-force로 순차 탐색해서 사방 중 더 낮은 물 빠진 곳이 있나 확인하는 local한 방식으로는
# 기존에 물 빠진 곳이 아니었던 위치가 물 빠진 곳이 되어, 그 옆 위치에 영향을 주는 연쇄적인 부분을 탐지하지 못함.
# 그래서 BFS로 물 빠짐이 확인된 곳에서부터 퍼져나가는 방식으로 탐색
drained = [[False] * M for _ in range(N)]
q = deque()

for i in range(N):
    for j in range(M):
        if drain[i][j]:
            drained[i][j] = True
            q.append((i, j))

directions = [(1,0), (-1,0), (0,1), (0,-1)]

while q:
    x, y = q.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not drained[nx][ny] and H[nx][ny] >= H[x][y]:
                drained[nx][ny] = True
                q.append((nx, ny))

# 물이 고인 칸(1) 표시
water = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not drained[i][j] and not drain[i][j]:
            water[i][j] = 1

# 누적합 계산
# 이게 1칸이 아니라 발 크기(hxw)만큼의 영역에서 검사를 해야하기 때문에
# 누적합 이용해서 prefixsum[우하단모서리] - prefixsum[좌상단모서리] 이렇게 해서 효율적으로 검사하기
ps = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        ps[i+1][j+1] = (ps[i][j+1] + ps[i+1][j] - ps[i][j] + water[i][j])

# 발 크기(h×w) 영역 검사
ans = 0
for i in range(N - h + 1):
    for j in range(M - w + 1):
        total = (ps[i+h][j+w] - ps[i][j+w] - ps[i+h][j] + ps[i][j])
        if total == 0:
            ans += 1

print(ans)
