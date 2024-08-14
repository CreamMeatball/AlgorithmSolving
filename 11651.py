import sys

N = int(sys.stdin.readline().rstrip())

numbers = []
for _ in range(N):
    numbers.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
numbers.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(numbers[i][0], numbers[i][1])