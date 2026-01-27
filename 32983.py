import sys
from collections import deque

input = sys.stdin.readline

N, M, C = map(int, input().rstrip().split())

S_r, S_c = map(int, input().rstrip().split())

# 1 기준 -> 0 기준 변경
S_r -= 1
S_c -= 1

board = []

for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

# 젤다(초록옷 아님)는 상관이 없고
# 램프 기준으로만 보면 됨

dist = [[-1] * M for _ in range(N)]
q = deque()
q.append((S_r, S_c))
dist[S_r][S_c] = 0

max_dist = 0
value_by_dist = [] # value_by_dist[n] = 램프로부터 거리가 n인 곳의 루피들의 총합
# BFS를 딱 한 번만 탐색하고, 이후 L값 늘리면서 미리 처리해뒀던 값으로 계산하기 위한 효율적 방법.

while q:
    r, c = q.popleft()
    d = dist[r][c]

    # 거리별 루피 합 저장
    if d == len(value_by_dist):
        value_by_dist.append(0) # 리스트 원소 늘리기
    value_by_dist[d] += board[r][c]

    max_dist = max(max_dist, d)

    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] != -1 and dist[nr][nc] == -1:
                dist[nr][nc] = d + 1
                q.append((nr, nc))

# L을 0부터 키워가며 최대 이윤 계산
max_profit = 0
current_sum = 0

# 각각의 L마다 따로 루프를 돌릴 필요가 없음
# L = N 은 N - 1까지의 값들도 다 포함하는 '누적합' 방식이기에
# 0 ~ 가능한 거리까지 루프 한 번만 돌면서 누적합으로 쌓아나가면서 최대값 갱신하면 됨
for L in range(len(value_by_dist)):
    current_sum += value_by_dist[L]
    profit = current_sum - L * C
    max_profit = max(max_profit, profit)

print(max_profit)
