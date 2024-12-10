n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))
    
dp = []
# for _ in range(n):
#     dp.append([0]*2)
    
# dp[0][0] = wine[0]
# dp[0][1] = wine[0]

# if n > 1:
#     dp[1][0] = dp[0][1] + wine[1]
#     dp[1][1] = wine[1]
    
# # [i][0] : 바로 전 거 마시고 이번 거 마시는 것. 이 때 참조되는 바로 전 거는 무조건 한 번 건너뛰고 마신 애(dp[i-1][1])여야 함.
# # [i][1] : 바로 전 거 건너뛰고 이번 거 마시는 것
# for i in range(2, n):
#     dp[i][0] = dp[i-1][1] + wine[i]
#     dp[i][1] = max(dp[i-2]) + wine[i]
    
# # print(dp)
# print(max(dp[n-1]))

# 위 방식으로 하면, 6 10 13 9 8 1 구조에서 마지막 와인을 억지로 마시려하니 오히려 효율이 안좋게 됨
# 그러면 안 마실 수 있는 선택지를 추가하자

for _ in range(n):
    dp.append([0]*3)
    
dp[0][0] = wine[0]
dp[0][1] = wine[0]
dp[0][2] = 0

if n > 1:
    dp[1][0] = dp[0][1] + wine[1]
    dp[1][1] = wine[1]
    dp[1][2] = max(dp[0])
    
for i in range(2, n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + wine[i]
    dp[i][1] = max(dp[i-2]) + wine[i]
    dp[i][2] = max(dp[i-1])
    
# print(dp)
print(max(dp[n-1]))
    
    