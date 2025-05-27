import sys

input_ = sys.stdin.readline

def isPalindrome(number):
    str_number = str(number)
    for i in range(len(str_number) // 2):
        if str_number[i] != str_number[-(i+1)]:
            return False
    return True

N = int(input_().rstrip())
numbers = [0] + list(map(int, input_().rstrip().split()))
dp = [[False] * (N + 1) for _ in range(N + 1)]

# dp를 이용해서 푼다 그러면
# 5개 길이짜리 수열이 있다고 하면
# 팰린드롬이란 건 양쪽 끝단으로 비교하는 것이기에
# 5개 길이 수열 팰린드롬 판단: 가운데 3개가 팰린드롬이었는지 판단 + 좌끝단과 우끝단이 같은지
# 로 판단하면 됨
# 그럼
# 4개 길이 수열 팰린드롬 판단: 가운데 2개가 팰린드롬이었는지 판단 + 좌끝단과 우끝단이 같은지
# ...
# 2개 길이 수열 팰린드롬 판단: 좌끝단과 우끝단이 같은지
# 1개 길이 수열 팰린드롬 판단: 무조건 팰린드롬

# -> 1개 길이 수열부터 시작해서 dp를 저장해놓고
# 더 큰 길이의 수열에서, 수열의 내부의 더 짧은 수열에 대한 이전 팰린드롬 판단 결과를 이용해서 팰린드롬 유무를 판단.

# # 길이 1
# for i in range(1, N + 1):
#     dp[i][i] = True

# # 길이 2
# for i in range(1, N):
#     if numbers[i] == numbers[i + 1]:
#         dp[i][i + 1] = True

# # 길이 3 이상
# for L in range(3, N + 1):
#     for i in range(1, N - L + 2):
#         j = i + L - 1
#         if numbers[i] == numbers[j] and dp[i + 1][j - 1]: # dp[i+1][j-1] 과 새로 추가된 양끝만 확인함으로써 이전에 확인했던 내용을 활용하여 효율적으로 계산
#             dp[i][j] = True

for L in range(1, N + 1): # 수열의 크기별로 케이스를 나눠 계산.
    for i in range(1, N - L + 2):
        j = i + L - 1
        if L == 1 or L == 2:
            if numbers[i] == numbers[j]:
                dp[i][j] = True
        else: # 길이가 3 이상
            if numbers[i] == numbers[j] and dp[i + 1][j - 1]: # dp[i+1][j-1] 과 새로 추가된 양끝만 확인함으로써 이전에 확인했던 내용을 활용하여 효율적으로 계산
                dp[i][j] = True
            
M = int(input_().rstrip())
for _ in range(M):
    S, E = map(int, input_().rstrip().split())
    print(1 if dp[S][E] else 0)