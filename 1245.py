import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

visited = [[False] * M for _ in range(N)]

# 주의: X좌표 차이와 Y좌표 차이가 1이하인 경우 인접이니, 대각선의 경우도 인접임.
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(x, y): # 입력받은 현재의 x, y가 peak인지 확인. 근데 visited 를 첨가해 중복 탐색을 없앤.
    q = deque([(x, y)])
    visited[x][y] = True
    is_peak = True
    
    while q:
        cx, cy = q.popleft()
        
        for i in range(8): # 주변 인접 8방향이 모두 자기보다 높은 게 없으면 is_peak = True. 근데 자신이랑 같은 높이를 만나면, 그것도 queue에 넣어서 한 덩어리로 탐색하는.
            nx, ny = cx + dx[i], cy + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] > board[cx][cy]:
                    is_peak = False
                elif board[nx][ny] == board[cx][cy] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return is_peak

ans = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if bfs(i, j):
                ans += 1

print(ans)