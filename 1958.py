str1 = list(str(input()))
str2 = list(str(input()))
str3 = list(str(input()))

len1 = len(str1)
len2 = len(str2)
len3 = len(str3)

dp = [[[0] * (len3 + 1) for _ in range(len2 + 1)] for _ in range(len1 + 1)]

for d in dp:
    print(d)
    
for i in range(1, len1):
    for j in range(1, len2):
        for k in range(1, len3):
            if str2[j] == str3[k]:
                dp[i][j][k] = dp[i][j][k - 1] + 1
            else:
                if dp[i][j][k - 1] > dp[i][j - 1][k]:
                    dp[i][j][k] = dp[i][j][k - 1]
                else:
                    dp[i][j][k] = dp[i][j - 1][k]
                    
for d in dp:
    print(d)
                
print(dp[-1][-1][-1])