import sys
import heapq

input = sys.stdin.readline

grid = [[0] * 501 for _ in range(501)]

# 위험한 구역(N개) 정보 입력 및 처리
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)
    
    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            grid[i][j] = 1

m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            grid[i][j] = 2

# 각 좌표의 상태(0: 안전, 1: 위험, 2: 죽음)

costs = [[float('inf')] * 501 for _ in range(501)]
costs[0][0] = 0

hq = []
heapq.heappush(hq, (0, 0, 0)) # (cost, r, c)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while hq:
    ccost, cr, cc = heapq.heappop(hq)
    
    if ccost > costs[cr][cc]:
        continue
    
    for d in directions:
        nr, nc = cr + d[0], cc + d[1]
        
        if not (0 <= nr < 501 and 0 <= nc < 501):
            continue
        
        if grid[nr][nc] == 2:
            continue
        
        ncost = ccost + grid[nr][nc]
        if ncost < costs[nr][nc]:
            costs[nr][nc] = ncost
            heapq.heappush(hq, (ncost, nr, nc))
            
if costs[500][500] == float('inf'): # inf == inf 연산 가능
    print(-1)
else:
    print(costs[500][500])