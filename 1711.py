# pypy3로 제출해야 시간초과 안 남.

import sys

input_data = sys.stdin.readline
N = int(input_data().rstrip())
point = []
for _ in range(N):
    point.append(list(map(int, input_data().rstrip().split())))
    
def isRightTriangle(point):
    for i in range(3):
        x1, y1 = point[i]
        x2, y2 = point[(i + 1) % 3]
        x3, y3 = point[(i + 2) % 3]
        vector1 = (x2 - x1, y2 - y1)
        vector2 = (x3 - x1, y3 - y1)
        inner_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        if inner_product == 0:
            return True
    return False

def pythagoras(point):
    a = (point[0][0] - point[1][0]) ** 2 + (point[0][1] - point[1][1]) ** 2
    b = (point[1][0] - point[2][0]) ** 2 + (point[1][1] - point[2][1]) ** 2
    c = (point[2][0] - point[0][0]) ** 2 + (point[2][1] - point[0][1]) ** 2
    for i in range(3):
        if a + b == c:
            return True
        a, b, c = b, c, a # good
    # sides = [a, b, c]
    # sides.sort()
    # if sides[0] + sides[1] == sides[2]:
    #     return True
    # 주의해야할게
    # a, b, c 구할 때 **0.5 했다가
    # a**2 + b**2 == c**2 이렇게 하면
    # 소수점 아래 특정 자릿수에서 잘렸다가, 그걸 다시 제곱을 해서 그런지
    # == 가 True 반환이 안되네.
    # 그래서 **0.5 연산 안 한 다음 그냥 a + b == c 이렇게 하니까 됨.
    return False

count = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            # if isRightTriangle([point[i], point[j], point[k]]):
            #     count += 1
            # if pythagoras([point[i], point[j], point[k]]):
            #     count += 1
            point1 = point[i]
            point2 = point[j]
            point3 = point[k]
            # 위처럼 point[i], point[j], point[k]를 변수로 초기화 해준 다음에
            # 아래에서 사용해야지 시간이 덜 걸림.
            # 리스트 내 index로 값 참조하는 건 O(1)밖에 안걸리지만
            # 똑같은 값을 반복해서 참조하는거면, 변수로 초기화 해놓고 사용하는 게 O(1)조차도 안걸려서 더 빠른 듯.
            not_max1 = 0
            not_max2 = 0
            a = (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
            max = a
            b = (point2[0] - point3[0]) ** 2 + (point2[1] - point3[1]) ** 2
            if b > max:
                not_max1 = max
                max = b
            else:
                not_max1 = b
            c = (point3[0] - point1[0]) ** 2 + (point3[1] - point1[1]) ** 2
            if c > max:
                not_max2 = max
                max = c
            else:
                not_max2 = c
            
            if not_max1 + not_max2 == max:
                count += 1
            # for _ in range(3):
            #     if a + b == c:
            #         count += 1
            #         break
            #     a, b, c = b, c, a # good
            
                
print(count)