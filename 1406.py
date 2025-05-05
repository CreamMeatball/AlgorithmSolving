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
            # right 의 왼쪽에 삽입하는 게 아니라
            # 그냥 오른쪽에 append 해놨다가
            # 나중에 반대로 꺼내는 식으로 (stack 방식)
            # 결국 list의 append, pop의 입출 방향을 반대로 쓰는 것과 같은 효과라고 볼 수도 있음 (deque의 popleft, appendleft 같은 효과)
    
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