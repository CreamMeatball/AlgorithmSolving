import sys
from collections import deque

input = sys.stdin.readline

n, T = map(int, input().rstrip().split())

positions = set()
for _ in range(n):
    positions.add(tuple(map(int, input().rstrip().split())))

def bfs():
    queue = deque([(0, 0, 0)])
    
    while queue:
        cx, cy, dist = queue.popleft()
        
        if cy == T:
            return dist
        
        # 현재 위치에서 이동 가능한 범위 탐색
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                nx, ny = cx + dx, cy + dy
                
                if (nx, ny) in positions:
                    queue.append((nx, ny, dist + 1))
                    positions.remove((nx, ny)) # 방문 처리

    return -1

print(bfs())