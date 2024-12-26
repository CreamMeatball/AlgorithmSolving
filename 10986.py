# import sys

# input_data = sys.stdin.readline

# N, M = map(int, input_data().split())
# A = list(map(int, input_data().split()))

# accum = [0 for _ in range(N)]

# count = 0

# for i in range(N):
#     accum[i] = A[i] if i == 0 else accum[i - 1] + A[i]
#     count += 1 if accum[i] % M == 0 else 0
#     # print(accum)
    
# for i in range(1, N):
#     temp = list(map(lambda x:x-A[i-1], accum))
#     accum = temp[1:]
#     for a in accum:
#         if a % M == 0:
#             count += 1

# print(count)

# 위 코드 시간초과 남

N, M = map(int, input().split())
A = list(map(int, input().split()))

remainder_count = [0] * M

prefix_sum = 0
for x in A:
    prefix_sum = (prefix_sum + x) % M
    # print(prefix_sum)
    remainder_count[prefix_sum] += 1
    
# remainder : 시작값이 첫번째값인 누적합에 대해 한 번만 누적합을 구하고, 그 누적합을 M으로 나눈 나머지가 몇이 되는 게 각각 몇 개씩 있다

# 나머지가 0인 prefix_sum은 그 자체로도 조건 만족
# remainder_count[0]개만큼 결과에 더해줌
result = remainder_count[0]

# 나머지가 같은 쌍을 고르는 조합 계산
for c in remainder_count:
    if c > 1:
        result += (c * (c - 1)) // 2 # 조합론. nC2 = n(n-1)
        # 하나의 나머지가 c번 등장했다면, 그 나머지를 가진 접두사 합 인덱스 중 서로 다른 두 인덱스(i < j)를 고르는 방법의 수가 nC2 = c × (c-1) / 2이기 때문이다.
        # 접두사 합이 같은 두 인덱스 사이의 부분 합은 M으로 나누었을 때 0이 되므로, 이 조합만큼 조건을 만족하는 연속 부분 구간이 생긴다.
        # ex) 나머지 1인 애의 개수가 3개(remainder_count[1] = 3)일 떄, '나머지1인애' - '나머지1인애' 를 하면 '나머지0인애' 가 됨.
        # 그렇기 떄문에 나머지 1인 애 3개 중 2개를 고르는 경우의 수가, 나머지 1인 누적합을 통해 나머지가 0인 부분합을 구하는 경우의 수가 되는 것임.
        # 2를 나눠서 순서를 없애는 이유는 '큰 누적합 - 작은 누적합'의 순서로 차를 구해야하기 때문.

print(result)