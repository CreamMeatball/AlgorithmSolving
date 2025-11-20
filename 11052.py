N = int(input())
Ps = [0] + list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(1, len(Ps)):
        if (i - j) >= 0:
            dp[i] = max(dp[i], dp[i - j] + Ps[j])
        
# print(dp)

print(dp[N])