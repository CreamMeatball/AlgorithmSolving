N = int(input())

if N == 1:
    print(3)
elif N == 2:
    print(7)
else:
    dp = [1 for _ in range(N + 1)]
    dp[1], dp[2] = 3, 7
    for i in range(3, N + 1):
        # 점화식 도출이 어려움
        dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901

    print(dp[N])