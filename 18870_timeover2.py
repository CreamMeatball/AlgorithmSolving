import sys

N = int(sys.stdin.readline().rstrip())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

sorted_set_numbers = sorted(set(numbers))
# 요건 오히려 시간 초과가 나지 않음!!

numbersOfnumbers = [0 for _ in range(N)]

for i in range(N):
    # 차례차례 정의해서 쓰는 게 중요.
    number_have_to_find = numbers[i]
    index_number_in_sorted_set = sorted_set_numbers.index(number_have_to_find)
    # 여기 때문에 시간 초과가 나는 것이었음. .index() 는 O(n)인데, 이게 반복문 안에 있으니 최대(중복이 없을 경우) O(N^2)이 되어버림.
    index = i
    numbersOfnumbers[index] = index_number_in_sorted_set

# for i in range(N):
#     print(numbersOfnumbers[i], end=' ')
    
print(' '.join(map(str, numbersOfnumbers)))