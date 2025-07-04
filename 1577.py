import sys
from collections import defaultdict

input_ = sys.stdin.readline

N, M = map(int, input_().rstrip().split())
K = int(input_().rstrip())

construction_roads = defaultdict(list)

for _ in range(K):
    a, b, c, d = map(int, input_().rstrip().split())
    # 양방향으로 저장
    construction_roads[(a, b)].append((c, d))
    construction_roads[(c, d)].append((a, b))

dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N + 1):
    for j in range(M + 1):
        if i == 0 and j == 0: # dp 0부터 시작해야할 때. 초기값 0일 때 탐색은 스킵해주기.
            continue
        
        if i > 0 and (i - 1, j) not in construction_roads[(i, j)]: # (i, j) 라는 도착지에 오기 위해 (i - 1, j) 에서 출발하는 경우를 따져보기
            dp[i][j] += dp[i - 1][j]

        if j > 0 and (i, j - 1) not in construction_roads[(i, j)]: # (i, j) 라는 도착지에 오기 위해 (i - 1, j) 에서 출발하는 경우를 따져보기
            dp[i][j] += dp[i][j - 1]

print(dp[N][M])