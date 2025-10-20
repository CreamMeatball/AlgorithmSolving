# PyPy3 for avoiding time exceed

import math

n = int(input())

dp = [0] * (n + 1)

for i in range(1, n + 1):
    if math.sqrt(i) % 1 == 0:
        # print(f"{i}'s sqrt: {math.sqrt(i)}")
        dp[i] = 1
        continue
    # for j in range(i - 1, 0, -1):
    #     temp = dp[j] + dp[i - j]
    #     # print(f"i: {i}. temp: dp[{j}]({dp[j]}) + dp[{i - j}]{dp[i - j]} = {temp}")
    #     if temp <= 4:
    #         dp[i] = temp
    #         break
    
    dp[i] = dp[i - 1*1] + 1
    if dp[i] == 2:
        continue
    # j = 1부터 하면 안되고, 꼭 기본값으로 dp[i] = dp[i - 1] + 1 해주고나서 j = 2 부터 해야함.
    j = 2
    while j*j <= i:
        temp = dp[i - j*j] + 1
        if temp < dp[i]:
            dp[i] = temp
        j += 1
            
# print(dp[1:n+1])
print(dp[n])