import sys

N = int(sys.stdin.readline().rstrip())

stack = []

for i in range(N):
    number = int(sys.stdin.readline().rstrip())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)
        
print(sum(stack))