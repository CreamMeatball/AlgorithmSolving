import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

max_height = max(map(max, graph))
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, rain, visited):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and graph[nx][ny] > rain:
                dfs(nx, ny, rain, visited)

for rain in range(max_height + 1):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > rain:
                dfs(i, j, rain, visited)
                count += 1

    result = max(result, count)

print(result)
