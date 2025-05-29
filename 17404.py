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
            dp[0][i] = costs[0][i]
        else: 
            dp[0][i] = float('inf')
    # 첫 값 설정
            
    for i in range(1, N):
        dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])
        
    dp[N - 1][c] = float('inf') # 마지막 집이 첫 집이랑 같은 경우는 불가능이므로.
        
    min_cost = min(min_cost, dp[N - 1][0], dp[N - 1][1], dp[N - 1][2])

print(min_cost)