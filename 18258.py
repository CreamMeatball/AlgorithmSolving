import sys
# list로 구현하면 시간 초과 나서 못 풀음
from collections import deque

que = deque()

def push(x):
    que.append(x)
    
def pop():
    # print(que.pop(0)) if que else print(-1)
    print(que.popleft()) if que else print(-1)
    
def size():
    print(len(que))

def empty():
    print(0) if que else print(1)
    
def front():
    print(que[0]) if que else print(-1)
    
def back():
    print(que[-1]) if que else print(-1)
    
commandListDict = {
    "push" : push,
    "pop" : pop,
    "size" : size,
    "empty" : empty,
    "front" : front,
    "back" : back
}

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    command = list(sys.stdin.readline().rstrip().split())
    
    if len(command) > 1:
        commandListDict[command[0]](int(command[1]))
    else:
        commandListDict[command[0]]()