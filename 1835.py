from collections import deque

N = int(input())
dq = deque()

# 역 순서로.
for i in range(N, 0, -1):
    dq.appendleft(i) # 책상에 올려놨던 카드를 다시 맨 앞에
    for _ in range(i):
        dq.appendleft(dq.pop()) # 뒤에서 앞으로 되돌림을 i번 반복

print(*dq)