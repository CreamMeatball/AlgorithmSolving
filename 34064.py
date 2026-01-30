import sys
from collections import deque

input = sys.stdin.readline

# 1차원적으로 생각하면 모든 시작위치로부터의 모든 도착위치까지를 BFS로 탐색한다,
# 이 과정 중에 이미 탐색한 위치라면 그걸 재활용한다.

# 이런 식으로 할 수 있을 거 같은데, 4차원 리스트 써야해서 시간, 메모라가 터짐.

# --->>
# BFS 탐색하면서, 이어져있으면 같은 땅이라고 치고,
# 또 다른 곳 탐색하다가, 새로운 땅 (안이어졌던)이면 또 거기서부터 탐색해가지고 또다른 같은 땅의 영역을 파악.
# --> 어떤 위치랑 어떤 위치가 이어져있냐 안이어져있냐를 확인.
# 그렇게 다 탐색하고 나서, 각 땅의 크기를 집계해서 카운팅.
# --> 이어져있기만하면 갈 수 있다는 것이기 때문.

N, M, K = map(int, input().rstrip().split())

# 0: 빈칸, -1: 별(장애물)
grid = [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
    r, c = map(int, input().split())
    grid[r][c] = -1
    
# 영역 정보 입력
a1, b1 = map(int, input().rstrip().split())
a2, b2 = map(int, input().rstrip().split())
a3, b3 = map(int, input().rstrip().split())
a4, b4 = map(int, input().rstrip().split())

# comp_map[r][c] 에 해당 칸의 구역 ID 저장
comp_map = [[0] * (M + 1) for _ in range(N + 1)]
comp_id = 1

# BFS를 이용해 연결 요소(구역) 나누기
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if grid[i][j] == 0 and comp_map[i][j] == 0:
            # 새로운 구역 발견, BFS 시작
            queue = deque([(i, j)])
            comp_map[i][j] = comp_id
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 1 <= nr <= N and 1 <= nc <= M:
                        if grid[nr][nc] == 0 and comp_map[nr][nc] == 0:
                            comp_map[nr][nc] = comp_id
                            queue.append((nr, nc))
            comp_id += 1

# 영역 1과 영역 2에서 각 구역 ID별 빈 칸 개수 집계
count1 = {}
for r in range(a1, a2 + 1):
    for c in range(b1, b2 + 1):
        cid = comp_map[r][c]
        if cid > 0: # 별이 아닌 경우만
            count1[cid] = count1.get(cid, 0) + 1
            
count2 = {}
for r in range(a3, a4 + 1):
    for c in range(b3, b4 + 1):
        cid = comp_map[r][c]
        if cid > 0: # 별이 아닌 경우만
            count2[cid] = count2.get(cid, 0) + 1

# 같은 구역 ID끼리 곱해서 합산
ans = 0
for cid in count1:
    if cid in count2:
        ans += count1[cid] * count2[cid] # 곱연산하면 경우의 수 나옴
        
print(ans)
