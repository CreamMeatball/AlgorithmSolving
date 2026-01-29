# 헝가리안 알고리즘 구현에 대해 다시 공부 필요

import sys
from collections import deque

input = sys.stdin.readline

A = []
for _ in range(4):
    A.append(list(map(int, str(input().rstrip()))))

B = []
for _ in range(4):
    B.append(list(map(int, str(input().rstrip()))))

# 기사와 목표 지점 좌표 리스트 생성
knights = [(r, c) for r in range(4) for c in range(4) if A[r][c] == 1]
targets = [(r, c) for r in range(4) for c in range(4) if B[r][c] == 1]
N = len(knights)

# BFS: 각 기사 위치에서 모든 칸까지의 최단 거리 계산
def get_dist(start_r, start_c):
    dist = [[-1] * 4 for _ in range(4)]
    dist[start_r][start_c] = 0
    q = deque([(start_r, start_c)])
    dr = [-2, -2, -1, -1, 1, 1, 2, 2]
    dc = [-1, 1, -2, 2, -2, 2, -1, 1]
    
    while q:
        r, c = q.popleft()
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < 4 and 0 <= nc < 4 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist

# 비용 행렬(Cost Matrix) 생성
# KM 알고리즘은 최대 가중치를 구하므로, 최소 거리를 구하기 위해 음수 처리
matrix = []
for kr, kc in knights:
    d_map = get_dist(kr, kc)
    row = []
    for tr, tc in targets:
        row.append(-d_map[tr][tc]) # 거리가 짧을수록 큰 값이 되도록 음수화
    matrix.append(row)

# KM 알고리즘 (헝가리안 알고리즘의 구현)
lx = [max(row) for row in matrix] # 왼쪽(기사) 기대치 (기사가 원하는 최단거리)
ly = [0] * N                     # 오른쪽(목표) 기대치 (인기 있는 목적지가 부르는 추가 비용)
match = [-1] * N                 # 매칭된 기사 인덱스 기록

def dfs(u, vis_x, vis_y, slack):
    vis_x[u] = True
    for v in range(N):
        if vis_y[v]: continue
        
        # 기대치와 실제 비용의 차이 (0이면 최적 경로)
        diff = lx[u] + ly[v] - matrix[u][v]
        
        if diff == 0:
            vis_y[v] = True
            # 비어있거나, 기존 임자가 양보 가능하다면
            if match[v] == -1 or dfs(match[v], vis_x, vis_y, slack):
                match[v] = u
                return True
        else:
            # 0이 아닐 경우, 나중에 기대치를 얼마나 줄여야 할지 기록
            slack[v] = min(slack[v], diff)
    return False

# 모든 기사에 대해 매칭 시도 
for i in range(N):
    slack = [float('inf')] * N
    while True:
        vis_x = [False] * N
        vis_y = [False] * N
        
        if dfs(i, vis_x, vis_y, slack):
            break # 매칭 성공 시 다음 기사로
            
        # 5. 매칭 실패 시 판 다시 짜기 (기대치 조정)
        # 0인 경로가 없으므로, slack 중 가장 작은 값만큼 기대치를 깎음
        d = min(slack[v] for v in range(N) if not vis_y[v])
        for j in range(N):
            if vis_x[j]: lx[j] -= d
            if vis_y[j]: ly[j] += d
            else: slack[j] -= d

# 결과 출력 (음수화했던 값을 다시 양수로 복구)
print(int(-(sum(lx) + sum(ly))))
