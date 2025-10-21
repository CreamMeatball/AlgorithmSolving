import sys

input = sys.stdin.readline

N = int(input().rstrip())
As = [0] + list(map(int, input().rstrip().split()))

dp = [float('inf')] * (N + 1)
dp[1] = 0

for i in range(1, N + 1):
    number = As[i]
    for jump in range(1, number + 1):
        idx = min(N, i + jump)
        dp[idx] = min(dp[idx], dp[i] + 1)

# print(dp[1:])
result = dp[N]
print(result if result != float('inf') else -1)