import sys

input = sys.stdin.readline

MOD = 1000000007
dp = [0] * 5001
dp[0] = 1

for i in range(2, 5001, 2): # i: 전체 길이
    for j in range(2, i + 1, 2): # j: 맨 처음 나타나는 완성된 괄호 뭉치의 길이. e.g. (()): 4
        # 이런 식으로 '맨 처음 나타나는 완성된 괄호 뭉치의 길이'로 기준을 잡으면 모든 경우를 다 셀 수 있으면서도 중복 없이 셀 수 있음.
        dp[i] = (dp[i] + dp[j - 2] * dp[i - j]) % MOD
        # dp[j - 2]: 괄호 묶음 '안'에서 발생할 수 있는 경우의 수
        # dp[i - j]: 괄호 묶음 '밖'에서 발생할 수 있는 경우의 수
        
# 발상 자체가 어려움

T = int(input().rstrip())

for _ in range(T):
    L = int(input().rstrip())
    print(dp[L] if L % 2 == 0 else 0)