x, y, w, h = map(int, input().split())
min_distance = 1000
if abs(x - w) < min_distance:
    min_distance = abs(x - w)
if abs(x - 0) < min_distance:
    min_distance = abs(x - 0)
if abs(y - h) < min_distance:
    min_distance = abs(y - h)
if abs(y - 0) < min_distance:
    min_distance = abs(y - 0)
    
print(min_distance)