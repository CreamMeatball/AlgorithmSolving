import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
apple_pos = []
for _ in range(K):
    apple_pos.append(tuple(map(int, input().rstrip().split())))
L = int(input().rstrip())
turns = {}
for _ in range(L):
    data = tuple(map(str, input().rstrip().split()))
    turns[int(data[0])] = str(data[1])
    
# print("apple_pos")
# print(apple_pos)
# print("turns")
# print(turns)

snake_body = deque([(1, 1)])
direction = (0, 1)
time = 0

while True:
    time += 1
    new_body = (snake_body[-1][0] + direction[0], snake_body[-1][1] + direction[1])
    # print(f"new_body: {new_body}")
    if new_body in snake_body or \
        (new_body[0] <= 0 or new_body[0] > N or new_body[1] <= 0 or new_body[1] > N):
        print(time)
        break
    snake_body.append(new_body)
    if new_body in apple_pos:
        apple_pos.remove(new_body)
    else:
        snake_body.popleft()
    if time in turns:
        d = turns[time]
        if (d == 'D' and direction == (0, 1)) or (d == 'L' and direction == (0, -1)):
            direction = (1, 0)  # 아래쪽
        elif (d == 'L' and direction == (0, 1)) or (d == 'D' and direction == (0, -1)):
            direction = (-1, 0)  # 위쪽
        elif (d == 'L' and direction == (-1, 0)) or (d == 'D' and direction == (1, 0)):
            direction = (0, -1)  # 왼쪽
        else:
            direction = (0, 1)  # 오른쪽