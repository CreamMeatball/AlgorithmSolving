from collections import deque

S = str(input())
T = str(input())

# 원래 S -> T 로 만들기 위해 BFS 사용했는데 시간 초과 남.

# 발상의 전환을 하기.
# S -> T 가 아닌 T -> S 를 만들기.

t_list = list(T) 

while len(t_list) > len(S):
    # 마지막 문자가 'A'인 경우
    if t_list[-1] == 'A':
        t_list.pop()
    # 마지막 문자가 'B'인 경우
    elif t_list[-1] == 'B':
        t_list.pop()
        t_list.reverse()
        
# S -> T 만들기 탐색을 하면 경우의 수가 2배로 발산하는데
# 현재의 두 가지 연산 조건 하에서는, T -> S 로 탐색한다면 끝자리가 A인지 B인지에 따라 경우의 수가 1개씩밖에 없게 됨.
# 그래서 발산하지 않고 하나의 경우를 유지하면서 수렴할 수 있음.

if "".join(t_list) == S: # 주의: list -> str 변환에서 str(list) 로 하면 안 됨.
    print(1)
else:
    print(0)