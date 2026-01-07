import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))
    
H, W, Sr, Sc, Fr, Fc = map(int, input().rstrip().split())

# 1-based index to 0-based index
Sr -= 1
Sc -= 1
Fr -= 1
Fc -= 1

# walls[i][j]: 누적합(효율 위해). the number of walls in the rectangle from (0,0) to (i,j)
walls = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        walls[i][j] = walls[i-1][j] + walls[i][j-1] - walls[i-1][j-1] + board[i-1][j-1]

def check_walls(r, c):
    r1, c1 = r + 1, c + 1
    r2, c2 = r + H, c + W
    
    count = walls[r2][c2] - walls[r1-1][c2] - walls[r2][c1-1] + walls[r1-1][c1-1]
    return count == 0

def bfs():
    dq = deque([(Sr, Sc, 0)])
    visited = [[False] * M for _ in range(N)]
    visited[Sr][Sc] = True
    
    while dq:
        r, c, dist = dq.popleft()
        
        if r == Fr and c == Fc:
            print(dist)
            return

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < N and 0 <= nc < M and nr + H <= N and nc + W <= M:
                if not visited[nr][nc]:
                    if check_walls(nr, nc):
                        visited[nr][nc] = True
                        dq.append((nr, nc, dist + 1))
    
    print(-1)

bfs()