N = int(input())
cards = list(map(int, input().split()))

dp = [1] * N

for now in range(1, N): 
    for before in range(now):
        if cards[before] < cards[now]:
            dp[now] = max(dp[now], dp[before] + 1)
            
print(max(dp))
