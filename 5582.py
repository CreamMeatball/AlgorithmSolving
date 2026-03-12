import sys

input = sys.stdin.readline

# LCS(최장 부분 수열) 문제: "부분 수열(subsequence)" --> 연속하지 않아도 됨
# 이 문제의 경우엔 연속해야 함.
# --> LCSubstring(최장 '공통' 부분 수열) 문제: "부분 문자열(substring)" --> 연속해야 함.

# LCSubstring과 LCS 구현의 차이 - 문자가 다를 때 처리 방식 차이:
# LCSubstring: $DP[i][j] = 0$
# LCS:         $DP[i][j] = \max(DP[i-1][j], DP[i][j-1])$

# 문자열 앞에 공백(' ')을 추가해 인덱스를 1부터 시작하게 만듦 (점화식 사용에서 index 때문에 헷갈리지 않게)
s1 = ' ' + input().rstrip()
s2 = ' ' + input().rstrip()

n1, n2 = len(s1) - 1, len(s2) - 1
dp = [0] * (n2 + 1)
ans = 0

for i in range(1, n1 + 1):
    new_dp = [0] * (n2 + 1)
    for j in range(1, n2 + 1):
        if s1[i] == s2[j]:
            new_dp[j] = dp[j-1] + 1
            if new_dp[j] > ans:
                ans = new_dp[j]
    dp = new_dp

# 바로 이전 행의 정보 하나만 기억하면 된다는 점을 이용해
# 1차원 DP로 정의한 뒤 행 내 정보를 덮어씌우는 방식을 이용해
# 2차원 DP가 아닌 1차원 DP로 풀 수 있음.

# https://www.interviewbit.com/blog/longest-common-substring/
# 위 링크 내 그림 참조
# (한국 웹에는 왜 LCS만 있고 LCString에 대한 그림 설명은 없는지 모르겠네)

print(ans)
