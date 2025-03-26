import sys

sys.setrecursionlimit(10**8)

input_data = sys.stdin.readline

N = int(input_data().rstrip())
coordinates = [list(map(int, input_data().split())) for _ in range(N)]
result = 0

# 한 턴마다 삼각형을 하나 뺀다지만
# 사실상 생각해보면
# 그냥 점 1개만 빼는 거임

def calculate_area(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    area = 1/2 * abs(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3)
    return area

def dfs(points):
    global result
    
    # 남은 점이 3개면 삼각형 넓이 계산
    if len(points) == 3:
        area = calculate_area(coordinates[points[0]], coordinates[points[1]], coordinates[points[2]])
        result = max(result, area)
        return
    
    n = len(points)
    for i in range(n):
        # 연속된 3개의 점 (시계 방향으로)
        # prev = points[(i-1) % n]
        # curr = points[i]
        # next = points[(i+1) % n]
        
        new_points = points[:i] + points[i+1:] # i번째 점 한 개 빼고 나머지를 새로 입력
        dfs(new_points)

initial_points_index = list(range(N))
dfs(initial_points_index)
print(result)