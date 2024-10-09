N = int(input())
point = []
for i in range(N):
    point.append(list(input().split()))
    
row_max, row_min = 0, 1000001
col_max, col_min = 0, 1000001

for i in range(N):
    row_max = max(row_max, int(point[i][0]))
    row_min = min(row_min, int(point[i][0]))
    col_max = max(col_max, int(point[i][1]))
    col_min = min(col_min, int(point[i][1]))
    
print((row_max - row_min) * (col_max - col_min))