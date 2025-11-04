number = [0] + list(int(x) for x in str(input()))
N = len(number) - 1

dp = [0] * (N + 1)
dp[0] = 1

for i in range(1, N + 1):
    if 1 <= number[i] and number[i] <= 9:
        dp[i] += dp[i - 1]
    two_number = int(str(number[i - 1]) + str(number[i]))
    if 10 <= two_number and two_number <= 34: # 1 <= 로 하면 안됨. 그러면 중복돼서 더해지게 됨.
        dp[i] += dp[i - 2]
        
# print(dp[1:])
print(dp[N])