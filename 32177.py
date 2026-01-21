from collections import deque

def can_airdrop(a, b, K, T):
    # a, b: (x, y, v)
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dist_sq = dx * dx + dy * dy
    return dist_sq <= K * K and abs(a[2] - b[2]) <= T

N, K, T = map(int, input().split())
Xp, Yp, Vp = map(int, input().split())

friends = []
photos = []

for _ in range(N):
    x, y, v, p = map(int, input().split())
    friends.append((x, y, v))
    photos.append(p)

nodes = [(Xp, Yp, Vp)] + friends

graph = [[] for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(i + 1, N + 1):
        if can_airdrop(nodes[i], nodes[j], K, T):
            graph[i].append(j)
            graph[j].append(i)

# BFS
visited = [False] * (N + 1)
queue = deque([0])
visited[0] = True

while queue:
    current = queue.popleft()
    for next in graph[current]:
        if not visited[next]:
            visited[next] = True
            queue.append(next)

result = []
for i in range(1, N + 1):
    if visited[i] and photos[i - 1] == 1:
        result.append(i)

if result:
    print(" ".join(map(str, result)))
else:
    print(0)
