import sys
input_data = sys.stdin.readline

T = int(input_data().rstrip())

for _ in range(T):
    n = int(input_data().rstrip())
    stickers = []
    stickers.append(list(map(int, input_data().rstrip().split())))
    stickers.append(list(map(int, input_data().rstrip().split())))
    
    # DP 배열 초기화
    dp = [[0] * n for _ in range(3)]
    
    # 선택의 가짓수가 3가지가 있는 dp 문제인 것.
    # 열 기준으로 세계관을 나눠 dp 구성
    
    # dp[0][i]: i번째 열에서 아무 스티커도 선택하지 않는 경우의 세계관
    # dp[1][i]: i번째 열에서 위쪽 스티커를 선택하는 경우의 세계관
    # dp[2][i]: i번째 열에서 아래쪽 스티커를 선택하는 경우의 세계관
    
    # 첫 번째 열 처리
    dp[0][0] = 0  # 아무 스티커도 선택 안함
    dp[1][0] = stickers[0][0]  # 첫 열의 위쪽 스티커 선택
    dp[2][0] = stickers[1][0]  # 첫 열의 아래쪽 스티커 선택
    
    # 나머지 열 처리
    for i in range(1, n):
        # 현재 열에서 아무것도 선택하지 않는 경우
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
        
        # 현재 열에서 위쪽 스티커를 선택하는 경우
        # dp[1][i] = max(dp[0][i-1] + stickers[0][i], dp[2][i-1] + stickers[0][i])
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + stickers[0][i]
        
        # 현재 열에서 아래쪽 스티커를 선택하는 경우
        dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + stickers[1][i]
    
    # 마지막 열에서의 최대 점수
    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))