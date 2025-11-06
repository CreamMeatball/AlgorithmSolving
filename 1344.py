Ap = float(input())/100
Bp = float(input())/100

# 18번 '독립시행'이니까
# 예를 들어, 7골을 넣을 확률은, 이전6골x(성공확률) + 이전7골x(실패확률)
# 인 것임.

dp = [[[0.0] * 19 for _ in range(19)] for _ in range(2)]
dp[0][0][0] = 1.0
dp[1][0][0] = 1.0

for team in range(2):
    prob = Ap if team == 0 else Bp
    for i in range(1, 19):
        for j in range(0, i + 1): # 0골일 확률로 해야하므로, 0부터 시작 (1부터 시작 X)
            dp[team][i][j] = dp[team][i - 1][j - 1] * prob + dp[team][i - 1][j] * (1 - prob)
            
# print(dp[0][18])
# print(dp[1][18])

# 2, 3, 5, 7, 11, 13, 17
not_primes = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18] # 0도 포함해야 함.

temp = 1.0
for np in not_primes:
    temp += dp[0][18][np] # 합연산!
A_prob = 1.0 - temp

temp = 1.0
for np in not_primes:
    temp += dp[1][18][np] # 합연산!
B_prob = 1.0 - temp

result_prob = 1 - A_prob * B_prob
print(result_prob)