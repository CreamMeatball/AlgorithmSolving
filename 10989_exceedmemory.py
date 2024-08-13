import sys

N = int(input())

numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))
    
sorted_numbers = sorted(numbers)

print('\n'.join(str(n) for n in sorted_numbers))