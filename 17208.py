import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

orders = []

for _ in range(N):
    orders.append(list(map(int, input().split())))

dp = [[-1] * (K + 1) for _ in range(M + 1)]
dp[0][0] = 0

for burger, fry in orders:
    for i in range(M, burger - 1, -1):
        for j in range(K, fry - 1, -1):
            dp[i][j] = max(dp[i][j], dp[i - burger][j - fry] + 1)

# for d in dp:
#     print(d)

print(max(max(d) for d in dp))
