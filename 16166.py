import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
lines = []

for _ in range(N):
    lines.append(set(list(map(int, input().rstrip().split()))[1:]))

dest = int(input().rstrip())

if dest == 0:
    print(0)
    sys.exit()

visited = [False] * N
q = deque()

for i in range(N):
    if 0 in lines[i]:
        q.append((i, 0))
        visited[i] = True

result = -1

while q:
    curr_idx, cnt = q.popleft()

    if dest in lines[curr_idx]:
        result = cnt
        break

    for next_idx in range(N):
        if not visited[next_idx]:
            if lines[curr_idx] & lines[next_idx]:
                visited[next_idx] = True
                q.append((next_idx, cnt + 1))

print(result)