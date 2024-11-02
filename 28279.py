import sys
from collections import deque

N = int(sys.stdin.readline())

dequelist = deque()

def one(x):
    dequelist.appendleft(x)
    
def two(x):
    dequelist.append(x)
    
def three():
    print(dequelist.popleft()) if dequelist else print(-1)
    
def four():
    print(dequelist.pop()) if dequelist else print(-1)
    
def five():
    print(len(dequelist))
    
def six():
    print(0) if dequelist else print(1)
    
def seven():
    print(dequelist[0]) if dequelist else print(-1)
    
def eight():
    print(dequelist[-1]) if dequelist else print(-1)
    
commandDict = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight
}

for _ in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    if len(command) == 1:
        commandDict[command[0]]()
    else:
        commandDict[command[0]](command[1])