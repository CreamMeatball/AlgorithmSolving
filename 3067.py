# 문제 9084랑 똑같음

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
                # 이렇게 되는 이유:
                # Total 경우의 수: "이전 동전 종류까지에서 가능했던 경우의 수" + "이번 동전을 통해 추가되는 새 경우의 수"
                # 일텐데,
                # "이번 동전을 통해 추가되는 새 경우의 수"가 'dp[i][m - coin_v]' 인 이유는
                # 딱 코인의 가치만큼 거슬러 올라갔을 때 가능한 경우여야지 경우의 수 +1 할 수 있기 때문.
                # 예를 들어 dp[5원][7] 이라면 dp[5원][7 - 5] = 0 일테고
                # dp[5원][5] 라면 dp[5원][0] = 1 일테니.
                # 이러한 알고리즘에 의해
                # j = 7인 경우는 5원으로 안 나눠떨어지니까 경우의 +0, j = 5인 경우는 5원으로 나눠떨어지니까 경우의 수 +1
                # 가 구조적으로 성립하게 됨 (또한 이것이 성립되기 위해 꼭 모든 행의 첫 번째 열은 1로 해놔야함)
            else:
                dp[i][m] = dp[i - 1][m] 
                
    # for d in dp:
    #     print(d)
        
    print(dp[N][M])