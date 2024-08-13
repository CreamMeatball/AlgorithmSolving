N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))
    
sorted_numbers = sorted(numbers)

print('\n'.join(str(n) for n in sorted_numbers))