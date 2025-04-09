import sys

input_data = sys.stdin.readline

N = int(input_data().rstrip())

# numbers = []

# for _ in range(N):
#     numbers.append(list(map(int, input_data().rstrip().split())))
    
# # print("numbers: ")
# # print(numbers)
    
# dp = [[0] * 3 for _ in range(N)]

# # max
# for i in range(N): # layer
#     if i == 0:
#         for j in range(3):
#             dp[i][j] = numbers[i][j]
#     else:
#         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + numbers[i][0]
#         dp[i][1] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + numbers[i][1]
#         dp[i][2] = max(dp[i - 1][1], dp[i - 1][2]) + numbers[i][2]

# # print("dp(max): ")
# # print(dp)

# # print("max: ")
# print(max(dp[N - 1]), end=' ')

# # min        
# dp = [[0] * 3 for _ in range(N)]        

# for i in range(N): # layer
#     if i == 0:
#         for j in range(3):
#             dp[i][j] = numbers[i][j]
#     else:
#         dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + numbers[i][0]
#         dp[i][1] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + numbers[i][1]
#         dp[i][2] = min(dp[i - 1][1], dp[i - 1][2]) + numbers[i][2]
        
# # print("dp(min): ")
# # print(dp)

# # print("min: ")
# print(min(dp[N - 1]))

# 메모리 초과 남.
# 최대한 덮어쓰면서 메모리 아껴보기

dp = []
dp2 = []

for i in range(N):
    data = list(map(int, input_data().rstrip().split()))
    if i == 0:
        dp.extend(data)
        dp2.extend(data)
        # print("dp: ", dp)
        # print("dp2: ", dp)
    else:
        select0 = max(dp[0], dp[1]) + data[0]
        select1 = max(dp[0], dp[1], dp[2]) + data[1]
        select2 = max(dp[1], dp[2]) + data[2]
        dp[0], dp[1], dp[2] = select0, select1, select2
        
        select0 = min(dp2[0], dp2[1]) + data[0]
        select1 = min(dp2[0], dp2[1], dp2[2]) + data[1]
        select2 = min(dp2[1], dp2[2]) + data[2]
        dp2[0], dp2[1], dp2[2] = select0, select1, select2
        
        # print("dp: ", dp)
        # print("dp2: ", dp2)
        
    if i == N - 1:
        print(max(dp), end=' ')
        print(min(dp2))