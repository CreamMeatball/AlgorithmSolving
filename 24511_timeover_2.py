import sys
from collections import deque

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

queuestackContainer = deque()

for i in range(N):
    queuestackContainer.append(B[i])
    
for i in range(M):
    x = C[i]
    for j in range(N):
        if A[j] == 0:
            temp = x
            x = queuestackContainer[j]
            queuestackContainer[j] = temp
        elif A[j] == 1:
            x = x
    print(x, end=' ')
    
# for i in range(N):
#     print(queuestackContainer[i].container)