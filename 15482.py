s1 = str(input())
s2 = str(input())

N = len(s1)
M = len(s2)

# LCS. subsequence -> 연속되지 않아도 됨.
# 1234567
# 1929394
# 이렇게 두 개면, LCS (최장 부분수열) 길이: 1234 -> 4.

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if s1[i-1] == s2[j-1]: # 현재 문자 같은지 확인. dp index가 1부터 시작하는데, string index는 0부터 시작이니까 -1 해서 맞춰줌.
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # s1에서 하나 뺀 거랑, s2에서 하나 뺀 거 중에 LCS 더 긴 거로 선택.

print(dp[N][M])