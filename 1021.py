import sys
from collections import deque

input_data = sys.stdin.readline

N, M = map(int, input_data().split())
target = list(map(int, input_data().split()))
queue = deque([i for i in range(1, N+1)])

count = 0
for i in target:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        elif queue.index(i) <= len(queue)//2: # 왼쪽으로 이동
        # elif queue.index(i) < len(queue)/2:
        # 로 써도 결과적으로 동일. 다만 짝수일 때, 찾고자 하는 값이 len(queue)//2에 위치할 떄, 위 식은 수를 왼쪽으로 이동시켜서 탐색, 이 식은 수를 오른쪽으로 이동시켜서 탐색.
        # 근데 횟수는 같아서 문제 없음.
            while queue[0] != i:
                queue.append(queue.popleft()) # 왼쪽 거 빼면서 오른쪽에 더하기.
                count += 1
        else:
            while queue[0] != i: # 오른쪽으로 이동
                queue.appendleft(queue.pop()) # 오른쪽 거 빼면서 왼쪽에 더하기.
                count += 1

print(count)