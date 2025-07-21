import sys

input = sys.stdin.readline

N = int(input().rstrip())
works = []
for i in range(1, N + 1):
    require, deadline = map(int, input().rstrip().split())
    works.append((deadline, require))

works.sort(reverse=True) # deadline이 먼 애부터

# 최대한 늦잠을 잔다 -> 마감시간에 딱 맞게 일을 끝낸다 (과제 밤 11시 59분에 내듯)
# -> deadline이 가장 멀찍이 있는 애를, 최대한 늦게 시작해서 딱 맞춰 끝낸다.
# -> 그 일의 시작 시간을 그 전 일의 종료 시간으로 두고, 앞 일을 또 최대한 뒤쪽으로 땡겨서 한다.
# -> ... 반복
# Greedy.
    
current_result = works[0][0] - works[0][1]
for i in range(1, N):
    deadline, require = works[i]
    if deadline < current_result: # deadline이 뒷 일을 최대한 미뤘을 때의 뒷 일 시작 시간보다 앞서있음.
        current_result = deadline - require
    else: # deadline이 앞서있지 않음 -> 현재 일을 최대한 뒤로 땡겨서 (뒷 일의 시작 시간에 종료되게끔) 하면 됨.
        current_result -= require
    
print(current_result if current_result >= 0 else -1)