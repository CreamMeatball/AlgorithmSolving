import sys

input = sys.stdin.readline

N, T = map(int, input().rstrip().split())

day_cost = []
penalty = []

for _ in range(N):
    d, m = map(int, input().rstrip().split())
    day_cost.append(d)
    penalty.append(m)
    
dp = [0] * (T + 1)
dp[0] = 0

for i in range(N):
    d, p = day_cost[i], penalty[i]
    for j in range(T, d - 1, -1):
        dp[j] = max(dp[j], dp[j - d] + p)
        
print(sum(penalty) - dp[T])