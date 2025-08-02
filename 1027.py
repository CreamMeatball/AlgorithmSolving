N = int(input())
buildings = [0] + list(map(int, input().split()))

def calAngle(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    return (y2 - y1) / (x2 - x1)

max_count = 0

for i in range(1, N + 1):
    point1 = (i, buildings[i])
    count = 0
    
    # left
    min_slope = float('inf')
    for l in range(i - 1, 0, -1):
        point2 = (l, buildings[l])
        slope = calAngle(point1, point2)
        if slope < min_slope:
            count += 1
            min_slope = slope
            
        
    # right
    max_slope = -float('inf')
    for r in range(i + 1, N + 1, 1):
        point2 = (r, buildings[r])
        slope = calAngle(point1, point2)
        if slope > max_slope:
            count += 1
            max_slope = slope
            
    max_count = max(max_count, count)
    
print(max_count)