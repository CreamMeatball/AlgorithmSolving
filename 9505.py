import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    K, W, H = map(int, input().split())
    costs = {'E': 0}
    for _ in range(K):
        name, val = input().split()
        costs[str(name)] = int(val)
        
    grid = []
    sy, sx = -1, -1
    for i in range(H):
        row = input().strip()
        grid.append(row)
        if 'E' in row:
            sy, sx = i, row.find('E')
                
    dist = [[float('inf')] * W for _ in range(H)]
    dist[sy][sx] = 0
    hq = [(0, sy, sx)]
    
    while hq:
        d, r, c = heapq.heappop(hq)
        
        if d > dist[r][c]:
            continue
            
        if r == 0 or r == H - 1 or c == 0 or c == W - 1:
            print(d)
            break
            
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W:
                nd = d + costs[grid[nr][nc]]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(hq, (nd, nr, nc))
