import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
field = [list(map(int, input().rstrip().split())) for _ in range(N)]
K = int(input())

visited = [[False] * M for _ in range(N)]
heap = []

# 일단 문제를 잘 이해해야하는게,
# 1. 민석이가 인접한 칸으로 이동하는 게 아님. 그냥 외곽쪽 혹은 옥수수가 캐진 곳에서부터 맘대로 이동하면서 캘 수 있는 거임.
# 소위 말해 '순간이동' 하면서 캐는 방식임.
# 2. 민석이가 'Greedy'하게 옥수수를 캔다고 되어있음. 옥수수 가치 총합이 높게끔 캐는 게 아님.
# 순간이동하면서 Greedy하게 캐는데, 그 경로가 어떻게 되냐는 거임.

# -> BFS와 heapq를 써야한다.

# 테두리 칸을 모두 넣기
for i in range(N):
    for j in range(M):
        if i == 0 or i == N - 1 or j == 0 or j == M - 1:
            heapq.heappush(heap, (-field[i][j], i, j))
            visited[i][j] = True

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

results = []
for _ in range(K):
    value, r, c = heapq.heappop(heap)
    results.append(f"{r + 1} {c + 1}")

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            visited[nr][nc] = True
            heapq.heappush(heap, (-field[nr][nc], nr, nc)) # 최소힙이라 -value

print('\n'.join(results))
