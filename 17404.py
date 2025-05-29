import sys

input_ = sys.stdin.readline

N = int(input_().rstrip())
costs = []
for _ in range(N):
    costs.append(list(map(int, input_().rstrip().split())))
    
dp = [[0] * (3) for _ in range(N)]
# 각 행에서 첫 열이 R, 둘쨰 열이 G, 셋째 열이 B

min_cost = float('inf')

for c in range(3): # 첫번째 집이 c번째 색을 고른 세계관
    for i in range(3):
        if c == i:
            dp[0][i] = costs[i]
        else: 
            dp[0][i] = costs[i]
    for i in range(1, N - 1):
        dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    if c == 0:
        dp[N - 1][0] = float('inf')
        dp[N - 1][1] = costs[N - 1][1] + min(dp[N - 2][0], dp[N - 2][2])
        dp[N - 1][2] = costs[N - 1][2] + min(dp[N - 2][0], dp[N - 2][1])
    elif c == 1:
        dp[N - 1][0] = costs[N - 1][0] + min(dp[N - 2][1], dp[N - 2][2])
        dp[N - 1][1] = float('inf')
        dp[N - 1][2] = costs[N - 1][2] + min(dp[N - 2][0], dp[N - 2][1])
    elif c == 2:
        dp[N - 1][0] = costs[N - 1][0] + min(dp[N - 2][1], dp[N - 2][2])
        dp[N - 1][1] = costs[N - 1][1] + min(dp[N - 2][0], dp[N - 2][2])
        dp[N - 1][2] = float('inf')
    print(dp[N - 1])
    if min(dp[N - 1]) < min_cost:
        min_cost = min(dp[N - 1])
        print(min_cost)

print(min_cost)