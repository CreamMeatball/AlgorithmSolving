import sys

input = sys.stdin.readline

N, T = map(int, input().rstrip().split())

cities = [(0, 0)]  # (0, 0) for dummy
special = [0] * (N + 1)  # first 0 for dummy

for i in range(1, N + 1):
    s, x, y = map(int, input().rstrip().split())
    cities.append((x, y))
    special[i] = s

# 미리 각 도시의 "가장 가까운 특별 도시까지의 거리"를 구해둠.
special_ids = [i for i in range(1, N + 1) if special[i]]
INF = 2001
near = [INF] * (N + 1)
if special_ids:
    for i in range(1, N + 1):
        if special[i]:
            near[i] = 0
        else:
            xi, yi = cities[i]
            md = INF
            for j in special_ids:
                xj, yj = cities[j]
                d = abs(xi - xj) + abs(yi - yj)
                if d < md:
                    md = d
            near[i] = md
            
# print(near[1:])

M = int(input().rstrip())
for _ in range(M):
    A, B = map(int, input().rstrip().split())
    direct = abs(cities[A][0] - cities[B][0]) + abs(cities[A][1] - cities[B][1])
    if special_ids:
        via_tp = near[A] + T + near[B] # 가장 가까운 특별 도시로 가서 텔포 거쳐서 가기.
        # 가까운 지하철 타고 간다고 생각하면 편함. near[A]: A에서 지하철 역까지 거리. T: 지하철 이동시간. near[B]: 내린 지하철 역에서 B까지의 거리.
        # 근데 이제 내린 곳 자체가 역이면 near 값이 0인 것.
        
        # 특별 도시에서는, 특별 도시인 곳 아무데나 고정 T 시간에 갈 수 있기 때문에
        # 어느 특별 도시로 가야하나 탐색할 필요 없이
        # 그냥 일단 가장 가까운 특별 도시로 가면 됨.
        
        print(min(direct, via_tp))
    else:
        print(direct)