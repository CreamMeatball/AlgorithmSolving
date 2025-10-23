N = int(input())

As = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if As[j] > As[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))