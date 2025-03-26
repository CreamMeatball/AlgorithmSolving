import sys
from itertools import combinations

input_data = sys.stdin.readline

N = int(input_data().rstrip())
coordinates = [list(map(int, input_data().split())) for _ in range(N)]
result = 0

def calculate_area(point1, point2, point3):
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3
    area = 1/2 * abs(x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3)
    return area

# 한 턴마다 삼각형을 하나 뺀다지만
# 사실상 생각해보면
# 그냥 점 1개만 빼는 거임

# 그리고 랜덤한 위치에서 점 1개를 뺀다는 건
# 결국 마지막에 랜덤한 위치의 점 3개만 남고
# 그 3개로 넓이 구하는 거 아님?
# 그러면 복잡한 계산 없이 랜덤한 3개 골라서 넓이 구하면 되나

# 3개의 점을 선택해서 삼각형 넓이 계산
for points in combinations(coordinates, 3):
    area = calculate_area(*points)
    result = max(result, area)
print(result)