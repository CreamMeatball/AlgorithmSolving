import sys

input = sys.stdin.readline

N = int(input().rstrip())

circles = []
for _ in range(N):
    circles.append(tuple(map(int, input().rstrip().split())))
    
circles.sort(key=lambda x: x[0])
# combinations 써서 모든 경우 쌍 다 해보면 시간 초과 남.
# x 위치 기준으로 정렬한 뒤에 인접한 것끼리만 비교.

def isInner(circle1, circle2):
    x1, r1 = circle1
    x2, r2 = circle2
    
    if abs(x1 - x2) < max(r1, r2):
        return True
    return False

for i in range(N - 1):
    
    circle1, circle2 = circles[i], circles[i + 1]
    
    if isInner(circle1, circle2): # 원이 내부에 들어있을 때
        if abs(circle1[1] - circle2[1]) > abs(circle1[0] - circle2[0]):
            # 안 겹침
            continue
        else:
            # 겹침
            break
    else: # 원이 외부에 있을 때
        if circle1[1] + circle2[1] < abs(circle1[0] - circle2[0]):
            # 안 겹침
            continue
        else:
            # 겹침
            break
else:
    print("YES")
    sys.exit()

print("NO")