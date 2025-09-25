import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

nodes = defaultdict(list)

for _ in range(N - 1):
    a, b, c = map(int, input().rstrip().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))

for _ in range(M):
    a, b = map(int, input().rstrip().split())

    dq = deque([])
    dq.append((a, 0))

    visited = [False] * (N + 1)

    while dq:
        cn, cc = dq.popleft()
    
        if visited[cn]:
            continue

        visited[cn] = True

        if cn == b:
            print(cc)

        for nn, nc in nodes[cn]:
            if not visited[nn]:
                dq.append((nn, cc + nc))
