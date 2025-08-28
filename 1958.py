# LCS (최장 공통 부분 수열)

str1 = list(str(input()))
str2 = list(str(input()))
str3 = list(str(input()))

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

str1 = [''] + str1
str2 = [''] + str2
str3 = [''] + str3

dp = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for _ in range(len1 + 1)]

# dp[i][j][k] 는 첫 번째 문자열의 앞 i글자, 두 번째 문자열의 앞 j글자, 세 번째 문자열의 앞 k글자까지 고려했을 때의 LCS 길이를 의미

# for d in dp:
#     print(d)
    
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        for k in range(1, len3 + 1):
            if str1[i] == str2[j] == str3[k]:
                dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1 # dp[i - 1][j - 1][k - 1]: 세 문자열의 현재 글자(str1[i], str2[j], str3[k])를 아직 포함시키지 않은 상태에서의 LCS 길이를 나타냄
                # dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1]) + 1
            else:
                dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
                    
# for d in dp:
#     print(d)
                
print(dp[-1][-1][-1])