import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

coins = [int(input().rstrip()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

# 루프 순서를 '동전 - 금액' 으로 해야함.
# 반대로 하면 조합이 아닌 순열처럼 세게 됨.
for c in coins:
    for i in range(1, k + 1):
        if i >= c:
            dp[i] += dp[i - c]
            
# print(dp)
print(dp[k])