N, K = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(K + 1)]
# 행: 고르는 개수
# 열: 만들어야 하는 값

for i in range(K + 1):
    dp[i][0] = 1

# for d in dp:
#     print(d)

# 숫자가 0 ~ N 까지 있을 때,
# 개수 K개의 숫자를 더해서 N이 되게하는 경우의 수

# dp 모르겠으면 그냥 실제 일일이 다 해서 표 작성해보기

#  n    1   2   3   4
# k 1   1   1   1   1
#   2   2   3   4   5 
#   3   3   6   10  15
#   4   ...

# => dp[i][j] = dp[i][j-1] + dp[i-1][j]

for i in range(1, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
# for d in dp:
#     print(d)

print(dp[K][N] % 1000000000)