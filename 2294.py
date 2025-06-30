import sys

input_ = sys.stdin.readline

INF = 10**10

n, k = map(int, input_().rstrip().split())
coins = [int(input_().rstrip()) for _ in range(n)]
# coins.sort(reverse=True)
coins = [0] + coins

# print(coins)

dp = [[0] + [INF] * (k) for _ in range(n + 1)]
# dp[i]: i번째 동전까지 봤을 때
# dp[:][k]: k원을 만들 때 사용한 동전의 개수

# for d in dp:
#     print(d)

min_count = INF
    
for i in range(1, n + 1):
    for j in range(1, k + 1):
        coin_value = coins[i]
        
        # i번째 동전을 사용하지 않는 경우. 이전 개수로 일단 초기화.
        dp[i][j] = dp[i - 1][j]
        
        if coin_value <= j:
            dp[i][j] = min(dp[i][j], dp[i][j - coin_value] + 1, dp[i - 1][j - coin_value] + 1)
            
    min_count = min(min_count, dp[i][k])
    
# for d in dp:
#     print(d)

if min_count > k:
    print(-1)
else:
    print(min_count)