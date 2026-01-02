import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, A, B = map(int, input().rstrip().split())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

visited = [False] * (N + 1)

# BFS로 A --> B 경로 탐색
q = deque()
q.append((A, 0, 0))  # (현재 노드, 거리 합, 경로 중 최대 간선)
visited[A] = True

# 어디 통로에서 만나는 게 가장 짧게 이동하는 건지 어떻게 아냐? --> 관점을 약간 다르게 보기.
# A --> B 최단 경로를 탐색한 다음에
# 그 최단 경로 내에 가장 길이가 길었던 통로 양단에서 만나면 됨.
# 가장 길이가 긴 통로 양단에서 만나는 경우가, 만나기 위해 가장 짧게 이동하는 경우임.
# 왜냐면 'A - B 간 최단길이 (경로 총 길이)' = 'A가 이동하는 거리' + '만나는 통로 거리' + 'B가 이동하는 거리'
# 이기 때문임.

while q:
    current, dist_sum, max_edge = q.popleft()

    if current == B:
        print(dist_sum - max_edge)
        break

    for cost, next in graph[current]:
        if not visited[next]:
            visited[next] = True
            q.append((next, dist_sum + cost, max(max_edge, cost)))
