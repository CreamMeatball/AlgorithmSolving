A, K = map(int, input().split())

dp = [float('inf')] * (K + 1)

dp[A] = 0

for i in range(A, K + 1):
    if i + 1 <= K:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    if 2 * i <= K:
        dp[2 * i] = min(dp[2 * i], dp[i] + 1)
        
# print(dp)
print(dp[K])