import sys
import math

input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
camps_x = [0] + list(map(int, input().rstrip().split()))
camps_y = [0] + list(map(int, input().rstrip().split()))

distances = [0.0] * N
for i in range(1, N):
    x1, y1 = camps_x[i], camps_y[i]
    x2, y2 = camps_x[i + 1], camps_y[i + 1]
    distances[i] = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 시간 효율성을 위해 누적합 이용 (N이 200000 이라 query마다 기울기 판단해서 계산해주면 시간 초과 남)
prefix_forward = [0.0] * (N + 1)
prefix_backward = [0.0] * (N + 1)

# 정방향 누적합 계산
for i in range(1, N):
    y1 = camps_y[i]
    y2 = camps_y[i + 1]
    
    distance = distances[i]
    
    cost_f = 0.0
    
    if (y2 - y1) > 0:
        cost_f = 3 * distance
    elif (y2 - y1) == 0:
        cost_f = 2 * distance
    else:
        cost_f = 1 * distance
        
    prefix_forward[i + 1] = prefix_forward[i] + cost_f
    
# 역방향 누적합 계산
for i in range(N - 1, 0, -1):
    y1 = camps_y[i + 1] # 오른쪽
    y2 = camps_y[i] # 왼쪽
    
    distance = distances[i]
    
    cost_b = 0.0
    
    if (y2 - y1) > 0:
        cost_b = 3 * distance
    elif (y2 - y1) == 0:
        cost_b = 2 * distance
    else:
        cost_b = 1 * distance
        
    prefix_backward[i] = prefix_backward[i + 1] + cost_b # [i + 1] = [i] + c 가 아닌, [i] = [i + 1] + c


for _ in range(Q):
    i, j = map(int, input().rstrip().split())
    
    if i < j:
        result = prefix_forward[j] - prefix_forward[i]
    else:
        result = prefix_backward[j] - prefix_backward[i]
        
    print(result)