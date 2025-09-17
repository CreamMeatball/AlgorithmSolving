numbers = list(map(int, input().split()))
numbers = numbers[:-1]

if not numbers:
    print(0)
    exit()

len_ = len(numbers)

# COST
# 중앙에서부터 다른 곳: 2
# 중앙 외 지점에서 인접한 지점(대각선 포함): 3
# 반대편으로: 4
# 같은 곳 다시: 1

# start = (0, 0)
INF = float('inf')

# 순서 / 왼발 / 오른발을 나눠서 3차원 DP로

dp = [[[INF] * (5) for _ in range(5)] for _ in range(len_ + 1)]
dp[0][0][0] = 0

directions_cost = [ # * 0은 출발할 때 말고 다신 안 쓰는 위치임.
    [1, 2, 2, 2, 2], # from 0 to (0, 1, 2, 3, 4)
    [0, 1, 3, 4, 3], # from 1 to (0, 1, 2, 3, 4)
    [0, 3, 1, 3, 4], # ...
    [0, 4, 3, 1, 3],
    [0, 3, 4, 3, 1]
]

for i in range(1, len_ + 1):
    target = numbers[i - 1] # numbers는 index 0부터 시작해서
    for l in range(5):
        for r in range(5):
            prev = dp[i - 1][l][r]
            l_cost = directions_cost[l][target]
            r_cost = directions_cost[r][target]
            if prev + l_cost < dp[i][target][r]:
                dp[i][target][r] = prev + l_cost
            if prev + r_cost < dp[i][l][target]:
                dp[i][l][target] = prev + r_cost
                
# for i in range(1, len_ + 1):
#     print(f"[[[ i: {i}. target: to {numbers[i - 1]} ]]]")
#     for l in range(5):
#         print(f"[l: {l}]")
#         print(f"{dp[i][l]}")
                
result = INF
for l in range(5):
    for r in range(5):
        result = min(result, dp[len_][l][r])
        
print(result)