import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

board = []
for _ in range(n):
    board.append(list(map(int, str(input().rstrip()))))

# "어디를 부숴야 최적일지를 고민한다"
# 라고 생각하면 너무 어려움.

# 벽이 없다고 생각하고 도착점까지 가되,
# "벽을 지날 경우 cost 1 을 지불한다 (cost 1을 누적시킨다)"
# 라고 생각하고 구현하면 됨.
# cost 지불하면서 지나가고, 그렇게 탐색한 모든 경로 중 cost 제일 낮을 게 정답.

visited = [[False] * n for _ in range(n)]

# 최단경로가 목적이 아닌, 벽을 최소한으로 부수는 게 목적이므로 (경로는 늘어나도 상관없음)
# 방향 탐색을 상, 하, 좌, 우 네 방향 다 탐색해야 함.
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(r, c, cost):
    dq = deque([[r, c, cost]])
    visited[r][c] = True
    
    while dq:
        cr, cc, cost = dq.popleft()
        if cr == n - 1 and cc == n - 1:
            return cost
        
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if (0 <= nr < n) and (0 <= nc < n) and not visited[nr][nc]:
                if board[nr][nc] == 0:
                    dq.append([nr, nc, cost + 1])
                else:
                    dq.appendleft([nr, nc, cost]) # 중요!!! append가 아닌 appendleft 로 해야함!!!. 너비 우선 탐색의 기조가 더 가까운/빠른 애가 앞쪽에 들어가서 먼저 pop된다 라는 것이기 때문에, 문제의 목적인 벽을 덜 깬 애가 앞에 오게끔 해야함.
                visited[nr][nc] = True
                
result = bfs(0, 0, 0)
print(result)