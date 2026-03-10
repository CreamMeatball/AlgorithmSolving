import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

n, m = len(a), len(b)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):51763
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(n + m - dp[n][m]) # A길이 + B길이 - LCS(최장공통부분수열)길이
