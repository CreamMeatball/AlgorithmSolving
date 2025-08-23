# [DP]
# n = int(input())

# dp = [0] * (n + 1)
# dp[1] = 1
# if n >= 2:
#     dp[2] = 2
    
# for i in range(3, n+1):
#     dp[i] = (dp[i-1] + dp[i-2]) % 10007

# print(dp[n] % 10007)


# [피보나치]
# n = int(input())
# MOD = 10007

# # 피보나치 F_{n+1} mod 10007 계산
# if n == 1:
#     print(1)
# else:
#     a, b = 1, 1  # F1=1, F2=1
#     for _ in range(2, n+1):
#         a, b = b, (a + b) % MOD
#     print(b)


# [조합 합]
import math

n = int(input())
MOD = 10007

result = 0
for k in range(0, n//2 + 1):
    result += math.comb(n-k, k)
    result %= MOD

print(result)