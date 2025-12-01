import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

satisfy = list(list(map(int, input().rstrip().split())) for _ in range(M))

# print(satisfy)
# print()

dp = [[0] * M for _ in range(N)]
for i in range(M):
    dp[0][i] = satisfy[i][0]

if M == 1:
    sum_ = satisfy[0][0]
    for i in range(1, N):
        sum_ += (satisfy[0][i] // 2)
    result = sum_
else:
    for i in range(1, N):
        for j in range(M):
            # 다른 거 고르는 경우
            if j == 0:
                temp1 = max(dp[i - 1][j+1:]) + (satisfy[j][i])
            elif j == M - 1:
                temp1 = max(dp[i - 1][:j]) + (satisfy[j][i])
            else:
                temp1 = max(max(dp[i - 1][:j]), max(dp[i - 1][j+1:])) + (satisfy[j][i])
            # 골랐던 거 또 고르는 경우
            temp2 = dp[i - 1][j] + (satisfy[j][i] // 2)
            dp[i][j] = max(temp1, temp2)
            
    result = max(dp[N - 1])
        
# for s in satisfy:
#     print(s)        

# print()
        
# for col in zip(*dp):
#     print(list(col))
        
print(result)