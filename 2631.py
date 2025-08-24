import sys

input = sys.stdin.readline

N = int(input().rstrip())

orders = [0] + [int(input().rstrip()) for _ in range(N)]

# 아이디어 떠올리기가 많이 어려움.

# 가장 긴 증가하는 부분수열(LIS)를 구한 뒤, 그 길이를 n에서 빼면 됨.
# [참고] https://velog.io/@soobin519/Python-%EB%B0%B1%EC%A4%80-2631-%EC%A4%84%EC%84%B8%EC%9A%B0%EA%B8%B0

# 가장 긴 증가하는 부분수열은, 이미 정렬할 필요가 없으니까 고정시키고
# 나머지 비정렬 수에 대해서, 각 수에 각 1번씩의 횟수를 사용하여 맞는 위치로 맞춰주면 됨.

dp = [1] * (N + 1)

# LIS 구하기
for i in range(1, N + 1): # 기존 LIS 최대값으로부터 연장시킬 타겟
    for j in range(1, i): # 기존 LIS 최대값
        if orders[j] < orders[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
# print(orders[1:])
# print(dp[1:])
print(N - max(dp))