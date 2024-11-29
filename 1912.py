# N = int(input())
# numbers = list(map(int, input().split()))
# maximum = -1001
# sum_temp = -1001

# for i in range(0, N):
#     for j in range(i, N):
#         # sum_temp = sum(numbers[i:j+1])
#         sum_temp += numbers[j]
#         if j == i:
#             sum_temp = numbers[j]
#         maximum = sum_temp if sum_temp > maximum else maximum
#     sum_temp -= numbers[i]
            
# print(maximum)

N = int(input())
numbers = list(map(int, input().split()))

for i in range(1, N):
    numbers[i] = max(numbers[i], numbers[i] + numbers[i-1])
    # 위 식은, (이전까지의 합 + 이번 숫자) > 이번 숫자, 이면 합산하겠단 뜻. 설령 이번 숫자가 음수일지라도.
    # 그렇다면 위의 합산되는 조건부가 깨질 때가 언제냐, 쭉 더해지다가, 지금까지의 전부의 합 < 이번 숫자일 때임.
    # 그 때가 되면, 합산 값이 없어지고 이번 숫자로 초기화 됨.
    # 결국, 이번 숫자가 이전 숫자들까지의 합보다 크다면, 이전 숫자들까지의 합은 버린다는 뜻임.
    # 동시에, 이후 숫자를 더할 경우 작아지는 경우도 방지할 수 있음.
    
print(max(numbers))
