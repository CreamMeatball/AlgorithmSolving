import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

smalls = set()

for _ in range(M):
    smalls.add(int(input().rstrip()))

# dp[i][v]: i번 돌에 도달했을 때 속도가 v였던 경우의 최소 점프 횟수
# 속도의 상한: 등차수열 합 공식 n(n+1)/2 = 10000 => n approx 141
# 따라서 속도는 150 정도면 충분함
MAX_V = int((2 * N)** 0.5) + 2
dp = [[float('inf')] * (MAX_V + 1) for _ in range(N + 1)]
# 이게 이전에 갖고 있던 속도를 가져가기 때문에
# N에 따른 1차원 visited로 안되고, 속도까지 반영한 2차원 visited로 해야됨.
# 같은 지점에 도착했어도, 현재 속도가 어떤지에 따라 다르기 때문에.

queue = deque()
# 1번 돌에서 2번 돌로 점프 (속도 1)
# 2번 돌이 작은 돌이면 갈 수 없음. 걍 실패.
if 2 not in smalls:
    dp[2][1] = 1
    queue.append((2, 1)) # (현재 위치, 현재 속도)

ans = -1

while queue:
    curr, step = queue.popleft()
    
    if curr == N:
        ans = dp[curr][step]
        break
    
    for x in [step - 1, step, step + 1]:
        if x > 0:
            next_stone = curr + x
            if next_stone <= N and next_stone not in smalls:
                if dp[next_stone][x] == float('inf'):
                    dp[next_stone][x] = dp[curr][step] + 1
                    queue.append((next_stone, x))

print(ans)