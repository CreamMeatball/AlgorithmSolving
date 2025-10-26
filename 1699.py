import math

N = int(input())

dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = float('inf')
    if math.sqrt(i) % 1 == 0:
        dp[i] = 1
        continue
    for j in range(1, N // 2 + 1):
        minus = j**2
        if minus < i:
            dp[i] = min(dp[i], dp[i - minus] + 1)
            # print(f"i: {i}, j: {j}, dp[1:]: {dp[1:]}")
        else:
            break
            
# print(dp[1:])
print(dp[N])