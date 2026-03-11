import sys

input = sys.stdin.readline

N = int(input().rstrip())
dp = [-1] * 50
dp[0] = 0

for _ in range(N):
    a = int(input().rstrip())
    if 500 < a < 20000:
        v = a - 500
        r = (v // 10) % 50
        new_dp = dp[:]
        for j in range(50):
            if dp[j] != -1:
                nxt = (j + r) % 50
                if dp[j] + v > new_dp[nxt]:
                    new_dp[nxt] = dp[j] + v
        dp = new_dp

print(dp[0])
