import sys

stack = []
commandIndex = None
x = None
    
    
# switch문을 Dictionary로 구현
        
def one(x):
    stack.append(x)

def two():
    if stack:
        print(stack[-1])
        stack.pop()
    else:
        print(-1)

def three():
    print(len(stack))
    
def four():
    if stack:
        print(0)
    else:
        print(1)
        
def five():
    if stack:
        print(stack[-1])
    else:
        print(-1)
            
commandDict = {
    1 : one,
    2 : two,
    3 : three,
    4 : four,
    5 : five
}
    

N = int(sys.stdin.readline().rstrip())
for i in range(N):
    command = list(map(int, sys.stdin.readline().rstrip().split()))
    
    if len(command) > 1:
        commandIndex = int(command[0])
        # print("commandIndex : ", commandIndex)
        x = int(command[1])
        # print("x : ", x)
    else:
        commandIndex = int(command[0])
        # print("commandIndex : ", commandIndex)
        
    commandDict[commandIndex](x) if len(command) > 1 else commandDict[commandIndex]()