from itertools import combinations

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
# numbers.sort()
# 원래 수열에서 연속된 수들의 합이라서, 정렬 안 하는 투 포인터 사용 필
# :r을 정해놓고, l을 키우는 방식.
# print(numbers)

l = 0
inter_sum = 0
count = 0

for r in range(N): # r: right
    inter_sum += numbers[r]
    while M < inter_sum and l <= r: # inter_sum이 M보다 더 크다면 inter_sum 줄이기
        inter_sum -= numbers[l]
        l += 1
    # loop 끝나면 inter_sum이 M이랑 동일하거나 더 작아져있는 상태
    if inter_sum == M:
        count += 1
        
print(count)