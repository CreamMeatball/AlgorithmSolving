import sys

input = sys.stdin.readline

D = int(input().rstrip())
MOD = 1000000007

dp = [0] * 8
dp[0] = 1

for _ in range(D):
    nxt = [0] * 8
    nxt[0] = (dp[1] + dp[2]) % MOD
    nxt[1] = (dp[0] + dp[2] + dp[3]) % MOD
    nxt[2] = (dp[0] + dp[1] + dp[3] + dp[4]) % MOD
    nxt[3] = (dp[1] + dp[2] + dp[4] + dp[5]) % MOD
    nxt[4] = (dp[2] + dp[3] + dp[5] + dp[7]) % MOD
    nxt[5] = (dp[3] + dp[4] + dp[6]) % MOD
    nxt[6] = (dp[5] + dp[7]) % MOD
    nxt[7] = (dp[4] + dp[6]) % MOD
    dp = nxt

print(dp[0])
