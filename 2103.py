import sys


input_ = sys.stdin.readline

N = int(input_().rstrip())

points_x = {}
points_y = {}
for _ in range(N):
    a, b = map(int, input_().rstrip().split())
    if a not in points_x:
        points_x[a] = []
    points_x[a].append(b)
    # if b not in points_y:
    #     points_y[b] = []
    points_y.setdefault(b, [])
    points_y[b].append(a)
    
total_x = 0
total_y = 0
    
# 같은 x에 있는 애들끼리 빼서 간격 더하기
for x, y in points_x.items():
    y.sort()
    for i in range(0, len(y) - 1, 2):
        total_y += y[i+1] - y[i]

# 같은 y에 있는 애들끼리 빼서 간격 더하기
for y, x in points_y.items():
    x.sort()
    for i in range(0, len(x) - 1, 2):
        total_x += x[i+1] - x[i]
        
print(total_x + total_y)

# [비고]
# 직교다각형에서는 모든 변이 수평·수직으로만 이어지고, 닫힌(closed) 경로(루프)를 이루기 때문에 다음 두 가지 관점에서 같은 x좌표를 갖는 꼭짓점의 개수는 반드시 짝수가 됩니다.

# 수직 변(Vertical edge)의 양 끝점 쌍
# – x = C라는 수직선 위에 놓인 변은 모두 수직 변입니다.
# – 수직 변 하나는 꼭짓점 두 개를 갖고, 그 두 꼭짓점의 x좌표는 같으므로 “한 변 → 두 개의 꼭짓점”으로 짝을 이룹니다.
# – 다각형을 이루는 모든 수직 변을 다 세면, 각 변마다 두 개씩 → 총 꼭짓점 수는 2×(수직 변 개수) = 짝수

# 닫힌 경로의 교차 짝(엔트리·이그지트)
# – 만약 x = C 위치에서 다각형의 내부를 훑어 내려간다고 할 때, “다각형 내부로 들어가는 지점”과 “다시 나오는 지점”이 번갈아가며 나타나야 경로가 닫히고 모순이 없습니다.
# – 들어가고 나오는 지점은 모두 꼭짓점 위에서 발생하므로, 반드시 한 쌍(짝)으로 등장
# – 따라서 그 x=C 선 위의 꼭짓점 수는 들어감·나옴 횟수 짝수 번 → 짝수

# 이 두 관점 모두 “수직 변이 하나의 쌍” 또는 “경로의 진입·이탈이 한 쌍”으로 취급되므로, 같은 x좌표를 가진 꼭짓점의 총 개수는 언제나 짝수임이 보장됩니다.