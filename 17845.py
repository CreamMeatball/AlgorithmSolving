import sys

# 쪼갤 수 없는 Knapsack 문제

input_ = sys.stdin.readline

N, K = map(int, input_().rstrip().split())

subjects = [(0, 0)]
for i in range(K):
    subjects.append(tuple(map(int, input_().rstrip().split())))
    
# print(subjects)
    
dp = [[0] * (N + 1) for _ in range(K + 1)]

for i in range(1, K + 1):
    for j in range(1, N + 1):
        importance, cost = subjects[i]
        if cost <= j:
            dp[i][j] = max( \
                dp[i - 1][j], # 이전 거 그대로 쓰는 게 낫다
                dp[i - 1][j - cost] + importance # 이전 거에서 이전 거 빼고 이번 거 새로 넣는 게 낫다
                )
        else:
            dp[i][j] = dp[i - 1][j]

# for d in dp:
#     print(d)
    
print(dp[K][N])