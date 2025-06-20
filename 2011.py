password = input()
N = len(password)

# dp[i] : 암호의 처음 i자리까지 해석할 수 있는 경우의 수
dp = [0] * (N + 1)
dp[0] = 1  # 아무 숫자도 해석하지 않은 경우 1가지

for i in range(1, N + 1):  # i자리까지 해석하는 경우
    # 한 자리 해석: 현재 자리의 숫자가 '0'이 아니면
    if password[i - 1] != '0':
        dp[i] += dp[i - 1] # 이전 경우의 수 유지
    # 두 자리 해석: i가 2이상이고, 앞자리가 '0'이 아니며, 
    # 두 자리 숫자가 10 이상 26 이하이면
    if i >= 2 and password[i - 2] != '0' and 10 <= int(password[i - 2:i]) <= 26:
        dp[i] += dp[i - 2] # 이전 경우의 수 + 전전 경우의 수(이전 경우에서 두 자리라고 했을 때)
    dp[i] %= 1000000

print(dp[N])