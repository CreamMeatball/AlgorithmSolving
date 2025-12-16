k, n = map(int, input().split())

if k == 0:
    print(0)
else:
    dp = [[0] * (k + n + 2) for _ in range(n + 1)]
    dp[0][k] = 1
    
    # 확률을 구해야되는 거라, max 혹은 min을 통해 최적으로 갱신해놓는 게 아니라, 모든 경우의 수를 다 저장해놔야됨.
    for i in range(n):
        for h in range(1, k + n + 1):
            if dp[i][h] == 0:
                continue
            
            if h - 1 > 0: # 위로 올라갔을 떄 죽지 않는 h일 경우
                dp[i+1][h-1] += dp[i][h]
            dp[i+1][h+1] += dp[i][h]
            
    print(sum(dp[n]))