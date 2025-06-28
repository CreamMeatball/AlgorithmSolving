n = int(input())
numbers = [0] + list(map(int, input().split()))

# dp = [[0] * (n + 1) for _ in range(n + 1)]

# # i: i번째 숫자를 제외했을 때
# # j: j번째 숫자까지 고려했을 때 최대값

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == i:
#             dp[i][j] = dp[i][j - 1]
#             continue
#         # dp[i][j] = max(dp[i][j - 1], dp[i][j - 1] + numbers[j])
#         dp[i][j] = max(numbers[j], dp[i][j - 1] + numbers[j])
        
# # for d in dp:
# #     print(d)

# max_ = 0
# for d in dp:
#     max_row = max(d)
#     max_ = max(max_row, max_)
    
# print(max_)

# 메모리 초과


# dp = [0] * (n + 1)

# max_ = 0

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == i:
#             dp[j] = dp[j - 1]
#             continue
#         dp[j] = max(numbers[j], dp[j - 1] + numbers[j])
#     max_i = max(dp)
#     max_ = max(max_i, max_)
    
# print(max_)

# 시간 초과 발생


dp = [[0] * (n + 1) for _ in range(2)]
# dp[0]: 숫자 제외 안 할 때
# dp[1]: 숫자 제외 할 때

# max_ = 0
max_ = -float('inf')
dp[0][0] = -float('inf')
dp[1][0] = -float('inf')
# ! 왜냐면 모든 숫자가 음수일 경우를 고려해야 됨.

for i in range(1, n + 1):
    dp[0][i] = max(numbers[i], dp[0][i - 1] + numbers[i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + numbers[i])
    # 와 레전드 이게 식이 되네
    # 설명:
    # dp[1][i] = max(이번 숫자를 뺐을 때의 값, 이전 어딘가의 숫자를 뺀 걸 유지한 상태로 이번 숫자를 이어서 더할 때의 값)
    max_ = max(max_, dp[0][i], dp[1][i])
    
# print(dp[0])
# print(dp[1])

print(max_)