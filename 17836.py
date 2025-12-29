import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

def bfs():
    q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    gram = float('inf')

    while q:
        x, y = q.popleft()
        dist = visited[x][y] - 1

        # 그람(검)을 찾은 경우: 현재까지 거리 + 공주까지의 직선 거리(맨해튼 거리)
        if board[x][y] == 2:
            gram = dist + (N - 1 - x) + (M - 1 - y)

        # 공주에게 도착한 경우: 직접 온 거리와 그람을 통해 온 거리 중 최소값 반환
        if x == N - 1 and y == M - 1:
            return min(dist, gram)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny] != 1: # 벽이 아니면 이동
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    
    return gram

result = bfs()
if result > T:
    print('Fail')
else:
    print(result)