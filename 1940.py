N = int(input())
M = int(input())
ingred = list(map(int, input().split()))

ingred.sort()

count = 0
left = 0
right = N - 1

while left < right:
    current_sum = ingred[left] + ingred[right]
    
    if current_sum == M:
        count += 1
        left += 1
        right -= 1
    elif current_sum < M:
        left += 1
    else:
        right -= 1

print(count)

# 투 포인터를 쓰면
# 이미 사용한 재료를 제거시키고 이럴 필요가 없네.

# 조합(Combination)이 필요한 문제에 투 포인터 적용하면 좋은 경우가 많은 듯.