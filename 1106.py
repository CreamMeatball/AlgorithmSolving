import sys

input_ = sys.stdin.readline

C, N = map(int, input_().rstrip().split())
info = [(0,0)] + [tuple(map(int, input_().rstrip().split())) for _ in range(1, N + 1)]
    
# knapsack 에제
# dp[i][c] = 용량 c 가방에서 i번째 물건까지 봤을 때 가능한 최대 가치

# def knapsack(weights, values, capacity):
#   n = len(weights)
#   dp = [[0] * (capacity + 1) for _ in range(n + 1)]
#
#   for i in range(1, n + 1):
#       w, v = weights[i - 1], values[i - 1]
#       for c in range(capacity + 1):
#           if w > c:
#               dp[i][c] = dp[i - 1][c]
#           else:
#               dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
#   return dp[n][capacity]

MAX_COST = C * 100

# dp = [[0] * (MAX_COST + 1) for _ in range(N + 1)]

# for i in range(1, N + 1):
#     cost, people = info[i]
#     for current_cost in range(MAX_COST + 1):
#         if cost > current_cost:
#             dp[i][current_cost] = dp[i - 1][current_cost]
#         else:
#             for j, c in enumerate(range(0, current_cost + 1, cost)):
#                 dp[i][current_cost] = max(dp[i - 1][current_cost], dp[i][current_cost], dp[i - 1][current_cost - c] + people * (j))

# min_cost = MAX_COST
# for row in dp:
#     for cost, people in enumerate(row):
#         if people >= C:
#             min_cost = min(min_cost, cost)

# print(min_cost)

# 시간 초과 발생.


# 무한 배낭 문제 (각 물건을 넣냐/안녛냐가 아닌, 각 물건을 무한히 담을 수 있다)

dp = [0] * (MAX_COST + 1)   # dp[cost]: cost 금액으로 얻을 수 있는 최대 고객수

for cost, people in info:
    for current_cost in range(cost, MAX_COST + 1):
        dp[current_cost] = max(dp[current_cost], dp[current_cost - cost] + people)
        # 제한이 없기 때문에, 물건을 넣냐 안 넣냐를 고민할 필요 없이, 그냥 이전의 최대값(dp)에 추가로 더 넣어서 최대값 갱신하는 방식.

# 최소 비용 추출
for cost, people in enumerate(dp):
    if people >= C:
        print(cost)
        break