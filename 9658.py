N = int(input())

# 9657 문제에서 승리/패배만 반전됨.

# 게임 이론에 입각하여 풀기 (9660.py)
    
# [DP로 풀어보기]

dp = [0] * (N + 1) # SK가 이기는 게 1, 지면 0
# dp[N]: 상근(SK) 입장에서, 이번 차례에 돌 N개를 받았다면, 내가 이기냐 여부.

dp[1] = 0
if N >= 2: dp[2] = 1
if N >= 3: dp[3] = 0
if N >= 4: dp[4] = 1 # 왜냐면 3개 가져가면 되니까

for i in range(5, N + 1):
    if (not dp[i - 1]) or (not dp[i - 3]) or (not dp[i - 4]): # 내가 1/3/4 개 가져가는 방법 중, 단 하나라도 상대가 지는 경우가 있을 경우
        dp[i] = 1
    else:
        dp[i] = 0
        
# print(dp[1:])
        
if dp[N] == 1: print('SK')
else: print('CY')