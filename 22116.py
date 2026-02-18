import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
board = [list(map(int, input().split())) for _ in range(N)]

# dist[r][c]는 (r, c)까지 도달하는 경로 중 "최대 경사"의 "최솟값"
dist = [[float('inf')] * N for _ in range(N)]
hq = []

dist[0][0] = 0
heapq.heappush(hq, (0, 0, 0))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 다익스트라

# 특이한 점은 일반적인 다익스트라가 특정 위치까지의 '누적' 거리의 최소를 구하는 것과 달리
# 이 문제는 경로 중 어느 '한 순간'의 최소값을 구하는 것임.
# 누적 경로 중의 '한 순간'의 최솟값을 구하는 데에도 다익스트라를 사용할 수 있다는 걸 보여줌.
# DP 느낌인 거.

# 어떤 특정한 (nr, nc) 위치에 도달할 때의 모든 경로 중에서, 경사의 최솟값을 어떻게 구하냐:
# 인접한 (r, c) 위치의 값이 항상 최솟값으로 보장되어 있다고 전제.
# 그래서 인접한 (r, c) 의 값이랑 비교한 차이값 하나를 통해서만 갱신하여 (nr, nc) 의 최소값을 보장받을 수 있음

while hq:
    d, r, c = heapq.heappop(hq)
    
    if d > dist[r][c]:
        continue
    
    if r == N - 1 and c == N - 1:
        print(d)
        break
    
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        
        if 0 <= nr < N and 0 <= nc < N:
            # 현재 칸과 다음 칸의 높이 차이(경사) 계산
            diff = abs(board[nr][nc] - board[r][c])
            
            if d > diff:
                cost = d
            else:
                cost = diff
                
            # 더 작은 최대 경사를 발견한 경우 갱신 및 큐에 삽입
            if dist[nr][nc] > cost:
                dist[nr][nc] = cost
                heapq.heappush(hq, (cost, nr, nc))