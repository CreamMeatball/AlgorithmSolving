import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # N: col, M: row
R, C = M, N

board = []
for _ in range(R):
    # board.append(list(int(x) for x in str(input().rstrip())))
    board.append(list(map(int, input().strip())))

# === Visualization ===
vis = False
if vis:
    vis_board = [[0] * C for _ in range(R)]

def visualization(r, c):
    print(f"--- r: {r}, c: {c} ---")
    for v in vis_board:
        print(v)
# =====================

# visited = [[False] * C for _ in range(R)]    
    
# dq = deque([])
# dq.append((0, 0, 0))

# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

# while dq:
#     count, r, c = dq.popleft()
#     # visited[r][c] = True
#     # 여기서 visited 하면 안됨. pop 된 이후에 visited 처리가 되기 때문에,
#     # pop 되기 전까진 같은 위치가 queue에 여러번 들어감.

#     # === Visualization ===
#     # vis_board[r][c] = count
#     # visualization(r, c)

#     if (r == R - 1) and (c == C - 1):
#         print(count)
#         break
    
#     for d in directions:
#         nr, nc = r + d[0], c + d[1]
#         if (0 <= nr < R) and (0 <= nc < C) and (not visited[nr][nc]):
#             # 0-1 BFS. popleft() 통해 값을 꺼낼 때, 꺼낸 값이 현재까지 중 가장 최적의 경로임이 보장됨.
#             if board[nr][nc] == 0:
#                 dq.appendleft((count, nr, nc))
#                 visited[nr][nc] = True
#             else:
#                 dq.append((count + 1, nr, nc))
#                 visited[nr][nc] = True

# === 더 일반적인 풀이 ===
INF = 10**9
dist = [[INF] * C for _ in range(R)]
dist[0][0] = 0

dq = deque([(0, 0)])
directions = [(-1,0), (1,0), (0,-1), (0,1)]

while dq:
    r, c = dq.popleft()
    d = dist[r][c]

    if r == R - 1 and c == C - 1:
        print(d)
        break

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            w = board[nr][nc] # 0 또는 1
            nd = d + w
            if nd < dist[nr][nc]: # 더 좋은 비용으로만 push
                dist[nr][nc] = nd
                if w == 0:
                    dq.appendleft((nr, nc))
                else:
                    dq.append((nr, nc))