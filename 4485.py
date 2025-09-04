import sys
import heapq

input = sys.stdin.readline

# 다익스트라
# 구현: heapq + Greedy
# Prim이랑 비슷하지만 약간 다름

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
problem_idx = 1

while True:
    N = int(input().rstrip())
    if N == 0:
        break
    
    board = [list(map(int, input().rstrip().split())) for _ in range(N)]
    
    distances = [[float('inf')] * N for _ in range(N)]
    distances[0][0] = board[0][0]
    queue = [(board[0][0], (0, 0))] # (거리, 노드)
    
    while queue:
        cd, (cr, cc) = heapq.heappop(queue)
        
        # 이미 처리된 노드라면 무시
        if cd > distances[cr][cc]:
            continue
        
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if (0 <= nr < N) and (0 <= nc < N):
                temp_dist = cd + board[nr][nc]
                # 더 짧은 경로를 발견하면 갱신
                if temp_dist < distances[nr][nc]:
                    distances[nr][nc] = temp_dist
                    heapq.heappush(queue, (temp_dist, (nr, nc)))
                    
    print(f"Problem {problem_idx}: {distances[N - 1][N - 1]}")
    problem_idx += 1