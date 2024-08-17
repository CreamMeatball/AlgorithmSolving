import sys

N = int(sys.stdin.readline().rstrip())

def factorial(n):
    if n == 0:
        return 1
    temp = 1
    for i in range(1, n+1):
        temp *= i
    return temp

answer = int(factorial(N) / factorial(N-2))

# print(factorial(N))

if N == 1:
    print(0)
else:
    print(answer)