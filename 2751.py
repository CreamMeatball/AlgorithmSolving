import sys

N = int(input())

numbers = []
for _ in range(N):
    # numbers.append(int(input()))
    # N이 100만 이하이므로, input() 대신 sys.stdin.readline() 사용해야만 시간 초과가 안 남.
    numbers.append(int(sys.stdin.readline().rstrip()))
    
sorted_numbers = sorted(numbers)

print('\n'.join(str(n) for n in sorted_numbers))