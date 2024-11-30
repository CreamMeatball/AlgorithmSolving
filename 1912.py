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
    
print(max(numbers))
