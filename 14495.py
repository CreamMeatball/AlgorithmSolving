n = int(input())

dp = [0] * 117
dp[1] = 1
dp[2] = 1
dp[3] = 1

if n <= 3:
    print(dp[n])
else:
    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-3]

    print(dp[n])