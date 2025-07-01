import sys
from collections import defaultdict

input_ = sys.stdin.readline

N = int(input_().rstrip())

counsels = [(0, 0)] + [tuple(map(int, input_().rstrip().split())) for _ in range(N)]
    
# 현재의 행동이
# 과거의 행동에 의존하는 게 아니라,
# 반대로, 미래의 행동을 강제시킴.
    
dp = [0] * (N + 2)
# i일까지의 최대값 X
# i일 아침일 때, 남은 잔여 기간에 대한 최대값.

for i in range(N, 0, -1): # 역으로 감.
    t, p = counsels[i]
    # print(i, t, p)
    do_counsel = 0
    if i + t - 1 <= N:
        do_counsel = dp[i + t] + p
    no_counsel = dp[i + 1]
    dp[i] = max(do_counsel, no_counsel)
    
# print(dp[1:N+1])

print(dp[1])