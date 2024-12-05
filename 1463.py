N = int(input())

# dp 푸는 법
# 더 작은 케이스에 대해 최적의 값(정답)을 구하고
# 더 큰 케이스의 정답을 구할 때, 구해놨던 더 작은 케이스에 대한 최적의 값을 사용한다

# 각 숫자에 대해 최소 연산 횟수를 저장할 배열
dp = [0] * (N + 1)
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
        
# print(dp)
print(dp[N])