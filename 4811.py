import sys

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    
    dp = [[0] * (N + 2) for _ in range(N + 1)]

    for h in range(N + 2):
        dp[0][h] = 1

    for w in range(1, N + 1):
        for h in range(N + 1):
            ways_W = dp[w - 1][h + 1] # 한조각짜리 하나 줄이고, 반조각짜리 하나 늘리고
            ways_H = 0
            if h > 0:
                ways_H = dp[w][h - 1] # 한조각짜리 개수는 그대로고, 반조각짜리 하나 줄이기
            dp[w][h] = ways_W + ways_H # * 두 가지 경우는 동시에 일어날 수 없음
            
    print(dp[N][0])