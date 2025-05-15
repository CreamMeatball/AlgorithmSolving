import sys

input_ = sys.stdin.readline

N = int(input_().rstrip())
coord = []
for _ in range(N):
    coord.append(list(map(int, input_().rstrip().split())))

# 벡터의 외적
# A X B = A벡터에서 B벡터로의 방향 기준 법선벡터. 크기: |A||B|sin(theta) (theta: A벡터에서 B벡터까지 반시계 방향으로 잰 각의 크기)

# Counter-Clockwise (CCW) 알고리즘은 2차원 평면에서 세 점의 방향성을 판별하는 알고리즘입니다. 주어진 세 점 P1, P2, P3가 시계 반대 방향(Counter-Clockwise, CCW), 시계 방향(Clockwise, CW), 또는 일직선 상에 있는지(Collinear)를 결정하는 데 사용됩니다.
# 핵심 원리:
# CCW 알고리즘은 주로 벡터의 외적(Cross Product) 개념을 이용합니다. 두 벡터  
# P1P2 와 P1P3 를 생각했을 때, 이 두 벡터의 외적 값의 부호에 따라 세 점의 방향성을 알 수 있습니다.

# P1 = (x1, y1)
# P2 = (x2, y2)
# P3 = (x3, y3)
# 라고 할 때, 벡터  
# P1P2 는 (x2−x1,y2−y1) 이고, 벡터 P1P3 는 (x3−x1,y3−y1) 입니다.
# 2차원 평면에서의 외적과 유사한 연산 (또는 2D 벡터를 3D 벡터 (x, y, 0)으로 확장하여 외적의 z 성분만 계산)은 다음과 같이 계산됩니다:
# CCW 값 = (x2−x1)(y3−y1)−(y2−y1)(x3−x1)
# 이 CCW 값의 부호에 따라 다음과 같이 판별합니다:
# CCW > 0: 세 점 P1, P2, P3는 시계 반대 방향으로 놓여 있습니다. (좌회전)
# CCW < 0: 세 점 P1, P2, P3는 시계 방향으로 놓여 있습니다. (우회전)
# CCW = 0: 세 점 P1, P2, P3는 일직선 상에 있습니다.
# 기하학적 의미:
# CCW 값은 P1, P2, P3 세 점이 이루는 삼각형의 (부호를 가진) 넓이의 2배와 같습니다. 만약 P1을 기준으로 P2를 거쳐 P3로 가는 경로가 좌회전이면 양수가 되고, 우회전이면 음수가 됩니다. 세 점이 일직선 위에 있다면 삼각형이 만들어지지 않으므로 넓이는 0이 됩니다.

def CCW(p1, p2, p3):
    """
    세 점의 방향성 및 값을 판별하는 함수 (Counter-Clockwise 알고리즘)

    Args:
    p1: 첫 번째 점의 좌표 (x, y) 튜플
    p2: 두 번째 점의 좌표 (x, y) 튜플
    p3: 세 번째 점의 좌표 (x, y) 튜플

    Returns:
    양수: 시계 반대 방향
    음수: 시계 방향
    0: 일직선
    
    Value:
    세 점을 통한 두 벡터가 이루는 평행사변형의 크기 (음수가 될 수 있음)
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    v1 = (x2 - x1, y2 - y1)
    v2 = (x3 - x1, y3 - y1)
    # v1 (P1P2) = (x2 - x1, y2 - y1)
    # v2 (P1P3) = (x3 - x1, y3 - y1)
    # v1 X v2 = v1x * v2y - v2x * v1y
    return v1[0] * v2[1] - v2[0] * v1[1]

area = 0
origin = (0, 0)
for i in range(N):
    p1 = coord[i]
    p2 = coord[(i + 1) % N]
    partial_area = CCW(origin, p1, p2)
    area += partial_area

area = abs(area) / 2
print(f"{area:.1f}")