import sys

input = sys.stdin.readline

T = int(input().rstrip())

dp = [[0] * 10 for _ in range(65)]
dp[1] = [1] * 10

# dp[i][j]: i자리 숫자이고 숫자 j로 끝나는 문제 조건 만족하는 경우의 수

for i in range(2, 65):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]
            # ex) dp[i][3] (j = 3)을 구하려면, 앞에서 0,1,2,3 으로 끝나는 경우의 수에 3을 더하는 거니까.

# 3 반복문으로 풀었지만
# 실제로 경우의 수 나열해보면
# 아래 형태로 점화식이 보인다고 함.
# dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
            
# for d in dp:
#     print(d)

for _ in range(T):
    n = int(input().rstrip())
    print(sum(dp[n]))