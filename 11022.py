import sys

T = int(sys.stdin.readline().rstrip())

numbers = [0 for _ in range(T)]

for i in range(T):
    numbers[i] = list(map(int, sys.stdin.readline().split()))
    
for i in range(T):
    print(f'Case #{i+1}: {numbers[i][0]} + {numbers[i][1]} = {numbers[i][0] + numbers[i][1]}')