import sys

input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    command_line = input().split()
    command = command_line[0]

    if command == "push":
        stack.append(int(command_line[1]))

    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif command == "size":
        print(len(stack))

    elif command == "empty":
        if not stack:
            print(1)
        else:
            print(0)

    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)