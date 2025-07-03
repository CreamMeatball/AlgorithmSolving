N = int(input())

items = []
for i in range(N):
    item = 2**i
    if item <= N:
        items.append(item)
    else:
        break
    
# print(items)

# 같은 걸 무한히 넣을 수 있는 Knapsack

# N = 1,000,000 이라서 2차원 배열 DP 쓰면 메모리 초과 남.
    
dp = [0] * (N + 1)
dp[0] = 1

for itm in items:
    for j in range(itm, N + 1):
        dp[j] = (dp[j - itm] + dp[j]) % 1000000000
        # dp[j] = ('이번멱수를 넣어서 대체할 때 경우' + '이전멱수를 통한 경우의 수') % MOD

# for d in dp:
#     print(d)
    
print(dp[N])