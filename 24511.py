import sys
from collections import deque

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

# consider only que
# concat in 'one' que
onlyque = deque()

for i in range(N):
    if A[i] == 0:
        onlyque.append(B[i])
    
for c in C:
    onlyque.appendleft(c)
    print(onlyque.pop(), end=' ')