import sys

input = sys.stdin.readline

D, P = map(int, input().split())

# default는 -1 과 같은 작은 값이고 dp[0]은 inf 값으로 설정해야하는 게 헷갈릴만한 요소
dp = [-1] * (D + 1)
dp[0] = float('inf')

for _ in range(P):
    L, C = map(int, input().split())
    for j in range(D, L - 1, -1):
        new = min(dp[j - L], C)
        if dp[j] < new:
            dp[j] = new
            
# print(dp)
print(dp[D])