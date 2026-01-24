from collections import deque
import sys
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())

# portal[x] = (type, destination)
portal = [None] * N
for _ in range(C):
    t, a, b = map(int, input().rstrip().split())
    portal[a] = (t, b)

INF = 10**18
dist = [INF] * N
dist[0] = 0

dq = deque()
dq.append(0)

while dq:
    x = dq.popleft()
    cur = dist[x]

    if x == N - 1:
        break

    # 포탈이 있는 칸
    if portal[x] is not None:
        t, b = portal[x]

        # 포탈 사용 (0초)
        if dist[b] > cur:
            dist[b] = cur
            dq.appendleft(b)

        # 블루 포탈이면 +1 이동도 가능
        if t == 1 and x + 1 < N:
            if dist[x + 1] > cur + 1:
                dist[x + 1] = cur + 1
                dq.append(x + 1)

    else:
        # 포탈이 없는 칸: 무조건 +1 이동
        if x + 1 < N and dist[x + 1] > cur + 1:
            dist[x + 1] = cur + 1
            dq.append(x + 1)

if dist[N - 1] == INF:
    print(-1)
else:
    print(dist[N - 1])