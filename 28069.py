from collections import deque

N, K = map(int, input().split())

# 상태: 현재 계단 번호 (0 ~ N)
# 이동:
# 1) +1
# 2) i + i//2

visited = [-1] * (N + 1)
q = deque()

visited[0] = 0
q.append(0)

min_steps = -1

while q:
    current = q.popleft()
    step = visited[current]

    if current == N:
        min_steps = step
        break

    # 다음 1칸 이동
    next = current + 1
    if next <= N and visited[next] == -1:
        visited[next] = step + 1
        q.append(next)

    # 지팡이 순간이동
    next = current + current // 2
    if next <= N and visited[next] == -1:
        visited[next] = step + 1
        q.append(next)

if min_steps != -1 and K >= min_steps:
    print("minigimbob")
else:
    print("water")
