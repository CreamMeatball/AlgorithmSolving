N = int(input())
A = list(map(int, input().split()))

# dp1 = [0] * N
# dp2 = [[0] * (i+1) for i in range(N)]

# for i in range(N):
#     dp1[i] = 1
#     for j in range(i):
#         if A[j] < A[i]:
#             dp1[i] = max(dp1[i], dp1[j] + 1)
            
# for i in range(N):
#     for j in range(j, i):
#         dp2[i][j] = 1
#         for k in range(j):
#             if A[k] < A[j]:
#                 dp2[i][j] = max(dp2[i][j], dp2[i][k] + 1)

# print(dp1)
# print(dp2)

# maximum = 0

# for i in range(N):
#     for j in range(i):
#         maximum = max(maximum, dp1[i] + dp2[i][j])
        
# print(maximum)

dp1 = [1] * N  # 증가 부분 수열 길이 저장
dp2 = [1] * N  # 감소 부분 수열 길이 저장

# 증가 부분 수열 계산
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

# 감소 부분 수열 계산 (역순으로 순회)
for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if A[j] < A[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
            
# dp2를, 반복문 시 index 0에서부터 증가하면서
# A[j] > A[i] 조건문을 통해
# 연속되는 감소 부분 수열의 길이를 계산하게 되면,
# 나중에 dp1과 dp2를 결합할 때 중복되는 부분이 발생하게 됨.
# dp2의 값이 맨 앞에서부터 계산한 값이기 때문에.

# 그래서 dp2를 뒤에서부터 역순으로 계산한 다음
# dp1과 dp2를 더하게 되면 편하게 답을 구할 수 있음.
# dp1은 왼쪽에서부터 계산, dp2는 오른쪽에서부터 계산해서 중간에서 만난다는 개념.

# print(dp1)
# print(dp2)

# 최대 길이 계산
maximum = 0
for i in range(N):
    maximum = max(maximum, dp1[i] + dp2[i] - 1)
# 1을 빼주는 이유는 dp1과 dp2 둘 모두에서 i번째 숫자가 포함돼서 중복되기 때문.

print(maximum)