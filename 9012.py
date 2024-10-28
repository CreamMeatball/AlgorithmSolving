import sys

T = int(sys.stdin.readline().rstrip())

# ( 가 stack 안에 존재하지 않는데 먼저 ) 가 나오는 경우 False
# 모든 문자열을 다 순회한 뒤, stack 안에 무언가가 남아있는 경우 False
for i in range(T):
    input_value = list(sys.stdin.readline().rstrip())
    stack = []
    is_VPS = True
    for j in input_value:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:
                is_VPS = False
                break
    if stack:
        is_VPS = False
    # print(stack)
    print("YES" if is_VPS else "NO")