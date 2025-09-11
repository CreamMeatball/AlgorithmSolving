N = int(input())
soldiers = list(map(int, input().split()))

# LIS 알고리즘 (내림차순으로)

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(N - max(dp))