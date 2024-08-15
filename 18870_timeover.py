import sys

N = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

sorted_set_numbers = sorted(set(numbers))

# set() 안 쓰고 중복 제거 하기
# sorted_numbers = sorted(numbers)
# sorted_set_numbers = []

# for i in range(N):
#     if sorted_numbers[i] not in sorted_set_numbers:
#         sorted_set_numbers.append(sorted_numbers[i])

# # 계수정렬을 이용하여 시간 복잡도도 줄이고, 중복 제거도 동시에 하기.
# sorted_numbers = [0 for i in range(2000000001)]

# for i in range(N):
#     sorted_numbers[numbers[i] + 1000000000] = 1
    
# sorted_set_numbers = [(sorted_numbers[i] - 1000000000 for i in range(2000000001) ) if sorted_numbers[i] == 1 else None]

numbersOfnumbers = [0 for _ in range(N)]

for i in range(N):
    # 차례차례 정의해서 쓰는 게 중요.
    number_have_to_find = numbers[i]
    index_number_in_sorted_set = sorted_set_numbers.index(number_have_to_find)
    # index_number_in_sorted_set = sorted_set_numbers.index(number_have_to_find)
    index = i
    numbersOfnumbers[index] = index_number_in_sorted_set

# for i in range(N):
#     print(numbersOfnumbers[i], end=' ')
    
print(' '.join(map(str, numbersOfnumbers)))