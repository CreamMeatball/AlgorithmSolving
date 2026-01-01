import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

virus_candidates = []
wall_cnt = 0
for r in range(N):
    for c in range(N):
        if board[r][c] == 2:
            virus_candidates.append((r, c))
        if board[r][c] == 1:
            wall_cnt += 1

# 벽을 제외한 모든 빈 칸(바이러스 놓을 수 있는 칸 포함)의 개수
total_empty_cnt = N * N - wall_cnt

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
result = float('inf')

def bfs(active_viruses):
    visited = [[False] * N for _ in range(N)]
    dq = deque()
    
    # 선택된 M개의 바이러스 위치를 큐에 넣고 시작 (row, col, time)
    for r, c in active_viruses:
        visited[r][c] = True
        dq.append([r, c, 0])
        
    infected_cnt = 0
    max_time = 0
    
    while dq:
        cr, cc, time = dq.popleft()
        max_time = max(max_time, time)
        infected_cnt += 1
        
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            
            if (0 <= nr < N) and (0 <= nc < N) and not visited[nr][nc]:
                if board[nr][nc] != 1: # 벽이 아니면 이동 가능.
                    visited[nr][nc] = True
                    dq.append([nr, nc, time + 1])
    
    # 모든 빈 칸에 바이러스가 퍼졌는지 확인
    if infected_cnt == total_empty_cnt:
        return max_time
    else:
        return float('inf')

# 그냥 바이러스 놓을 수 있는 위치에 대해 combination으로 다 해보기.
# 바이러스를 놓을 수 있는 위치 중 M개를 뽑는 모든 조합에 대해 시뮬레이션
# 문제에서 '2의 개수는 10보다 작거나 같다' 고 주어졌기 때문에, 최악의 경우인 10C5 의 경우에도 252 이기 떄문에 시간 초과가 발생하지 않음.
for comb in combinations(virus_candidates, M):
    time = bfs(comb)
    result = min(result, time)

if result == float('inf'):
    print(-1)
else:
    print(result)