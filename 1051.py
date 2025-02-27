import sys
input_data = sys.stdin.readline

N, M = map(int, input_data().split())
grid = [input_data().strip() for _ in range(N)]

max_area = 1

for i in range(N):
    for j in range(M):
        for k in range(1, min(N, M)):
            if i + k >= N or j + k >= M:
                break
            if grid[i][j] == grid[i+k][j] and grid[i][j] == grid[i][j+k] and grid[i][j] == grid[i+k][j+k]:
                area = (k+1) * (k+1)
                if area > max_area:
                    max_area = area
                    
print(max_area)