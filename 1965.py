n = int(input())
boxes = list(map(int, input().split()))

# LIS (최장 증가 부분 수열)
# -> DP

dp = [1] * (n)

for i in range(n):
    for j in range(i): # i에서의 dp값을 최대값으로 만들어줌
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
# print(dp)
# print(dp[n - 1]) <- 아님. dp[i]: 무조건 i번째 상자를 포함시킨다는 전제에서의 최대값
print(max(dp))