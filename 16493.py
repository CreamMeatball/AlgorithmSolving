import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

costpage = []

for _ in range(M):
    costpage.append(tuple(map(int, input().rstrip().split())))
    
# KnapSack 문제임
# 0/1 냅색 알고리즘

dp = [0] * (N + 1)

# 1. 모든 챕터에 대해서 반복 (Items)
for day_cost, page_value in costpage:
    # 2. 날짜를 거꾸로 반복 (N일부터 day_cost일까지)
    # 역순으로 돌려야 이번 챕터를 중복해서 더하는 것을 방지할 수 있음
    for i in range(N, day_cost - 1, -1):
        dp[i] = max(dp[i], dp[i - day_cost] + page_value)

print(dp[N])