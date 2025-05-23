import sys

input_data = sys.stdin.readline

init_str = str(input_data().rstrip())

# 그 때마다 string 새롭게 메모리 할당해서 자르고 이어붙이는 게 비효율적이니
# 애초에 커서 기준으로 왼/오 stack 2개로 나눠서 저장해놓자

left_stack = list(init_str)  # 커서 왼쪽의 문자들
right_stack = []  # 커서 오른쪽의 문자들

M = int(input_data().rstrip())
for _ in range(M):
    command = input_data().rstrip()
    
    if command[0] == 'L':
        if left_stack:  # 커서가 맨 앞이 아니면
            right_stack.append(left_stack.pop())
            # right stack의 왼쪽으로 삽입하는 게 아니라
            # 그냥 오른쪽으로 append 및 pop으로 진행하고,
            # 나중에 꺼낼 때 반대로 꺼내는 식으로.
            # 왼쪽이 입출구인 stack을 오른쪽이 입출구인 stack이 되는 효과라고 볼 수도 있음 (deque의 popleft, appendleft 가 되는 것 같은 효과)
    
    elif command[0] == 'D':
        if right_stack:  # 커서가 맨 뒤가 아니면
            left_stack.append(right_stack.pop())
    
    elif command[0] == 'B':
        if left_stack:  # 커서가 맨 앞이 아니면
            left_stack.pop()  # 왼쪽 스택의 마지막 문자 삭제
    
    elif command[0] == 'P':
        left_stack.append(command[2])  # 왼쪽 스택에 문자 추가

result = ''.join(left_stack + right_stack[::-1]) # 오른쪽 파트는 역순으로 꺼내기 (stack)
print(result)