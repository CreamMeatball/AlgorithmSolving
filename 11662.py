import math

# Convex한 형태에서의 삼분탐색!

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy = map(int, input().split())

# 시간 t: (0 <= t <= 1) 라고 전제 (normalized value)

def get_position(t):
    # 민호의 위치
    minho_x = Ax + t * (Bx - Ax) # t가 1일 때 Bx
    minho_y = Ay + t * (By - Ay)
    # 강호의 위치
    kangho_x = Cx + t * (Dx - Cx)
    kangho_y = Cy + t * (Dy - Cy)
    return minho_x, minho_y, kangho_x, kangho_y

def get_distance_squared(t):
    mx, my, kx, ky = get_position(t)
    return (mx - kx)**2 + (my - ky)**2

# !!!!! 두 사람의 거리 D(t)는 항상 'Convex한 형태'의 함수임 !!!!!

# 삼분 탐색 시작
start, end = 0.0, 1.0 # 거리가 최소가 되는 시간 t를 찾기 위해, 삼분탐색 (ternary search) 이용.
# 이분탐색이 아니라, 삼분탐색인 이유:
# 단조 함수나 정렬된 배열에서는, 한쪽 방향으로 일관되게 커지기(작아지기) 때문에
# 중간값을 탐색했을 때, 이제 어느 구간을 탐색해야할지를 알 수가 있는데
# 현재 같은 Convex한 함수(Unimodal function)일 때는
# 어느 시점부터 다시 커지는지(작아지는지)를 모르기 때문에
# 이분이 아닌 삼분을 한 뒤, 좀 더 낮은 값을 보이는 포인트 쪽으로 반복 탐색을 진행함.
# like 딥러닝에서의 SGD (Stochastic Gradient Descent).

# 100번의 반복으로 충분한 정밀도를 얻을 수 있음
for _ in range(100): # 정답 레이블이 있는 것이면, 'while (정답과의 차이가 오차 범위 초과일 경우)' 로 하면 되는데, 현재는 언제가 최소지점인지 모르니, 적당히 큰 값으로 반복.
    m1 = start + (end - start) / 3 # 시간이 m1 일 때 (삼등분 후 start에 가까운 시점)
    m2 = end - (end - start) / 3 # 시간이 m2 일 때 (삼등분 후 end에 가까운 시점)
    
    dist1_sq = get_distance_squared(m1) # 시간이 m1인 순간에서의 둘의 거리
    dist2_sq = get_distance_squared(m2) # 시간이 m2인 순간에서의 둘의 거리
    
    if dist1_sq < dist2_sq: # 삼등분 했을 때 start 에 가까운 시점에서의 거리가 더 가까웠다면 (D(m1) < D(m2) 였다면)
        end = m2 # 이후 [start, m2] 구간에서 재탐색
    else:
        start = m1 # 이후 [m1, end] 구간에서 재탐색

min_distance = math.sqrt(get_distance_squared(start))

print(f"{min_distance:.10f}")