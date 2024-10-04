def is_factor(number):
    if number == 1:
        return 0
    for i in range(2, number):
        if number % i == 0:
            return 0
    return 1

N = int(input())
numbers = list(map(int, input().split()))
# print(numbers)

count = 0

for number in numbers:
    if is_factor(number):
        count += 1
    else:
        continue
    
print(count)