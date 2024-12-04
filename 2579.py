N = int(input())
stair = []
stair.append(0)
for _ in range(N):
    stair.append(int(input()))

dp = [[0,0] for _ in range(N+1)]
# dp[i][0] = i-1번째 계단을 밟고, i번째 계단을 연속해서 밟은 경우
# dp[i][1] = i-1번째 계단을 밟지 않고, i번째 계단을 밟은 경우(바로 전 계단을 건너뛴 경우)

# i번째 계단을 밟을 때,
# i-1번째 계단을 밟을 때의 값이 i-2번째 계단도 밝고 올라왔을 때의 값을 쓸 수 없음
# 반대로 i-1번째 계단을 밟을 때의 값이 i-2번째 계단을 밟지 않고 올라왔을 때의 값이라면, i-1번째 계단의 값이 그 간 어떤 과정을 밟아본 값이든 상관 없이 쓸 수 있음
for i in range(1, N+1):
    if i == 1:
        dp[i][0] = dp[i][1] = stair[i]
    elif i == 2:
        dp[i][0] = dp[i-1][0] + stair[i]
        dp[i][1] = stair[i]
    else:
        dp[i][0] = dp[i-1][1] + stair[i]
        dp[i][1] = max(dp[i-2]) + stair[i]
        
print(max(dp[N]))