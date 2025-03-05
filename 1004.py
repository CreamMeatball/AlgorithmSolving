import sys

input_data = sys.stdin.readline

T = int(input_data())

for _ in range(T):
    count = 0
    x1, y1, x2, y2 = map(int, input_data().split())
    n = int(input_data())
    
    for i in range(n):
        cx, cy, cr = map(int, input_data().split())
        
        dist_square_1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        dist_square_2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        
        if (dist_square_1 < cr**2 and dist_square_2 > cr**2) or ( dist_square_1 > cr**2 and dist_square_2 < cr**2):
            count += 1
            
    print(count)