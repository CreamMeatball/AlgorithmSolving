import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

must_pass = []
for _ in range(m):
    must_pass.append(list(map(int, input().rstrip().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

# 현재 행에서, 무조건 지나야하는 위치가 포함된 행이라면
# : 현재 행에서, 무조건 지나야하는 위치를 제외한 타 위치는 모두 dp값을 0으로

# 처음엔 그냥 DP 일반적으로 다 초기화 한 뒤
# 마지막에 수학적으로 곱연산으로 계산해줘야했는데, 그게 안됨

for i in range(1, n):
    filter = -1
    for mp in must_pass:
        if mp[0] == i:
            filter = mp[1]
    for j in range(n):
        if filter != -1 and j != filter:
            dp[i][j] = 0
            continue
        if j == 0:
            dp[i][j] = dp[i - 1][j]
        elif j == n:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            
result = sum(dp[n - 1])
print(result)