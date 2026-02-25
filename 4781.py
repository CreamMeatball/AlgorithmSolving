# PyPy3 (time exceed)

import sys

input = sys.stdin.readline

# 무한 배낭(Knapsack) 문제 (물건을 무한으로 담을 수 있음)

while True:
    n, m = input().split()
    n = int(n)
    m = int(float(m) * 100 + 0.5)
    
    if n == 0 and m == 0:
        break
    
    dp = [0] * (m + 1)
    
    for _ in range(n):
        c, p = input().rstrip().split()
        c = int(c)
        p = int(float(p) * 100 + 0.5)

        # 중요!!! 사탕을 무한으로 반복 살 수 있는 문제이기에 정순으로 loop 진행.
        # 정순으로 진행하게 될 경우, 같은 사탕을 여러번 살 수 있는 효과가 생김.
        # 그렇지 않은 문제의 경우 (중복 참조 불가능해야할 경우) 역순으로 loop 돌아야 함.
        for j in range(p, m + 1):
            if dp[j] < dp[j - p] + c:
                dp[j] = dp[j - p] + c
                
    print(dp[m])
