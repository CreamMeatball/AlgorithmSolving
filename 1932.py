n = int(input())

triangle = []
for i in range(n):
    triangle.append(list(map(int, input().split())))
    
dp = []
for i in range(n):
    dp.append([0] * (i + 1))
    
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 각 줄에서 맨 앞 숫자일 때
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        elif j == i: # 가구 줄에서 맨 뒤 숫자일 때
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]
        else: # 나머지의 경우
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            
print(max(dp[n-1]))