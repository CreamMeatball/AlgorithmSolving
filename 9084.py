import sys

input_ = sys.stdin.readline

T = int(input_().rstrip())

for _ in range(T):
    N = int(input_().rstrip())
    coin_value = list(map(int, input_().rstrip().split()))
    coin_value.sort(reverse=True)
    coin_value = [0] + coin_value
    M = int(input_().rstrip())
    
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1 # 0원을 만드는 경우의 수: 아무것도 안 내기 1가지 (중요)
    # dp[i][w]: i번째 물건까지만 고려할 때, 가방제한이 w일 때의 최대 경우의 수
    
    # 같은 물건을 무한히 넣을 수 있는 knapsack 알고리즘
    
    for i in range(1, N + 1):
        coin_v = coin_value[i]
        for m in range(1, M + 1):
            # 점화식: dp[i][m] = dp[i - 1][m] + dp[i][m - coin_v]
            if coin_v <= m:
                dp[i][m] = dp[i - 1][m] + dp[i][m - coin_v]
            else:
                dp[i][m] = dp[i - 1][m] 
                
    # for d in dp:
    #     print(d)
        
    print(dp[N][M])
    