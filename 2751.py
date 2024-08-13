N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))
    
sorted_numbers = sorted(numbers)

for i in range(len(sorted_numbers)):
    print(sorted_numbers[i])