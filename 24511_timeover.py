import sys
from collections import deque

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

queuestackContainer = deque()

class queuestack:
    def __init__(self, type):
        self.type = type
        self.container = deque()
        
    def pop(self):
        if self.type == 0:
            return self.container.popleft()
        elif self.type == 1:
            return self.container.pop()
    
    def push(self, x):
        self.container.append(x)
        
for i in range(N):
    queuestackContainer.append(queuestack(A[i]))
    queuestackContainer[i].push(B[i])
    
for i in range(M):
    x = C[i]
    for j in range(N):
        queuestackContainer[j].push(x)
        x = queuestackContainer[j].pop()
    # for j in range(N):
    #     print(queuestackContainer[j].container, end=' ')
    # print()
    print(x, end=' ')
    # print()
    
# for i in range(N):
#     print(queuestackContainer[i].container)