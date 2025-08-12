import sys

input = sys.stdin.readline

n = int(input().rstrip())
points = list(tuple(map(int, input().rstrip().split())) for _ in range(n))
# print(points)

# x, y랑 위치를 임의로 설정한 뒤에
# 반복문 돌리면서 모든 거리 차이 다 계산해서
# 최종 최소값을 찾는 건 너무 오래 걸림. O(10^11).

# 최소 거리 구하는 방식이 맨해튼 거리라서
# x랑 y를 따로 봐서 계산하자.
# 그리고 주어진 고객들의 위치를 정렬한 뒤에, 그 값들의 중간값으로 설정하면, 그게 수학적으로 거리가 최소가 되는 값임.

# 감각적으로 생각했을 때
# 예를 들어, 중앙보다 왼쪽에 치우친 위치로 편의점 위치 설정을 했다.
# 그러면 그 편의점을 왼쪽으로 한 칸씩 옮길 때마다,
# 왼쪽에 있는 고객들은 한 칸씩 가까워질 거고
# 오른쪽에 있는 고객들은 한 칸씩 멀어질텐데
# 초기 편의점 위치보다 왼쪽에 존재하는 고객 수 < 초기 편의점 위치보다 오른쪽에 존재하는 고객 수
# 이기 때문에
# 변화된 거리 차이의 총합은 더 커지게 되어있음.

# 그래서 결국 중앙에 해야됨.
# 그리고 또 위의 예시를 통해 생각해보면,
# 거리 차이의 합이 최소가 되게 하는 위치는
# 중앙값을 포함하여, 여러 곳이 될 수 있음.

points.sort(key=lambda x: x[0])
x = points[n//2][0]

points.sort(key=lambda x: x[1])
y = points[n//2][1]

sum = 0
for p in points:
    delta_x = abs(x - p[0])
    delta_y = abs(y - p[1])
    sum = sum + delta_x + delta_y
    
print(sum)