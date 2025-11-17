# import math

N, K = map(int, input().split())

# print(math.factorial(N)/(math.factorial(K)*math.factorial(N - K)) % 10007)

# 위 방식 쓰면
# type의 유효숫자 한계상 연산 과정 중의 매우 큰 숫자가 잘리거나 (ex. 너무 커져버리면 2.567e+2567 같이 되면서 뒤쪽 작은 자릿수의 숫자가 짤림)
# (1000! = 4 * 10^2567 이라 자릿수가 2568 이라고 함. 우주에 존재하는 모든 원자의 개수 10^80 보다 훨씬 큰..)
# 너무 큰 숫자들 다 계산해서 구한다음에 나누느라 시간 초과 난다고 함
# -> DP 이용해서 매번 10007로 나눠서 나머지 값만 남기면서 연산하자

MOD = 10007

dp = [[0] * (N + 1) for _ in range(N + 1)]

for n in range(N + 1):
    for k in range(n + 1):
        if k == 0 or k == n:
            dp[n][k] = 1
        else:
            dp[n][k] = (dp[n-1][k-1] + dp[n-1][k]) % MOD

print(dp[N][K])