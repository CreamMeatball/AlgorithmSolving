def calculate_distance(inputdata):
    x1, y1, r1, x2, y2, r2 = map(int, inputdata)
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if distance == 0 and r1 == r2:
        return -1
    elif distance == 0 and r1 != r2:
        return 0
    elif distance > r1 + r2 or distance < abs(r1 - r2):
        return 0
    elif distance == r1 + r2 or distance == abs(r1 - r2):
        return 1
    elif distance < r1 + r2:
        return 2

N = int(input())
for i in range(N):
    inputdata = list(map(int, input().split()))
    result = calculate_distance(inputdata)
    print(result)
    
    
