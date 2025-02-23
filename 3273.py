# from itertools import combinations

n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

count = 0

# nCr = list(combinations(numbers, 2))
# for i in nCr:
#     if sum(i) == x:
#         count += 1
        
# print(count)

# 투 포인터 학습을 위해 라이브러리 쓰지 않고 구현

i, j = 0, n - 1
numbers.sort() # 투 포인터 사용을 위해 필수

while i < j:
    sum_of_two = numbers[i] + numbers[j]
    if sum_of_two == x:
        count += 1
        i += 1
        j -= 1
    elif sum_of_two < x:
        i += 1
    else:
        j -= 1
        
print(count)