import sys

input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

dp = [1] * (N + 1)
MOD = 1000000007

for _ in range(7):
    next = [0] * (N + 1)
    for u in range(1, N + 1):
        curr_val = dp[u]
        for v in adj[u]:
            next[v] += curr_val
    dp = [x % MOD for x in next]

print(sum(dp[1:]) % MOD)
