import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input().rstrip())
    arr_str = input().rstrip()
    
    if n == 0:
        dq = deque()
    else:
        dq = deque(arr_str[1:-1].split(','))
        
    rev = False # 효율화 핵심. 진짜로 뒤집기 반복해버리면 너무 오래 걸리니, 읽는 방향에 대한 변수로만 체크 --> 효율 극대화
    err = False
    
    for cmd in p:
        if cmd == 'R':
            rev = not rev
        elif cmd == 'D':
            if not dq:
                err = True
                break
            if rev:
                dq.pop()
            else:
                dq.popleft()
                
    if err:
        print("error")
    else:
        if rev:
            dq.reverse()
        print("[" + ",".join(dq) + "]")
