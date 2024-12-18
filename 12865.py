N, K = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(K+1)]

for item in items:
    w,v = item
    for i in range(K,w-1,-1):
        # dp[i] : i 무게일 때 최대 가치
        dp[i] = max(dp[i],dp[i-w]+v)

print(dp[-1])