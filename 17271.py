N, M = map(int, input().split())

MOD = 1000000007

dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    dp[i] = dp[i - 1]
    if i >= M:
        dp[i] += dp[i - M]
    dp[i] %= MOD

print(dp[N])