N, K = map(int, input().split())
caffeines = list(map(int, input().split()))

# 0/1 냅색

dp = [float('inf')] * (K + 1)
dp[0] = 0

for c in caffeines:
    for i in range(K, c - 1, -1): # 역순. 자신을 더한 값에 또 자신을 더하는 것을 막는 trick.
        dp[i] = min(dp[i], dp[i - c] + 1)
        
if dp[K] >= float('inf'):
    print(-1)
else:
    print(dp[K])