N = int(input())

numbers = []
require = 5

for i in range(N):
    numbers.append(int(input()))
    
for i in range(N):
    require1 = 4
    require2 = 4
    for j in range(N):
        if numbers[i] < numbers[j] and numbers[i] + 5 > numbers[j]:
            require1 -= 1
        elif numbers[i] > numbers[j] and numbers[i] - 5 < numbers[j]:
            require2 -= 1
            
    require = min(require, require1, require2)
    
print(require)