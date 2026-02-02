# PyPy3

import math

N = int(input())
R = N // 2
R_sq = R * R

# 기본적으로
# 1) x방향으로 지나는 개수만큼 무조건 테두리가 그려진 개수가 있고
# 2) y방향으로 지나는 개수만큼 테두리가 그려진 개수가 있음

# 이 때 첫 시작 포인트에서는 1) 과 2) 가 중복으로 세지므로, -1 해줌

# 또한, 만약 테두리(접하는 부분 제외한)가 정확히 grid의 교차점 포인트에 딱 지나갈 경우,
# 테두리가 그려진 칸이 없게 되므로
# 테두리가 grid 교차점 포인트에 딱 지나는 경우, count - 1 해줘야됨

minus_count = 0

limit = int(R / (2**0.5)) # 시간 초과 때문에 한 사분면에서도 또 절반 잘라서(y=x) 1/8만 세서 집계함

for x in range(1, limit + 1):
    y_pow = R_sq - x * x
    y = math.isqrt(y_pow)
    
    if y * y == y_pow:
        if x < y:
            # (x, y)가 정수해면 대칭점인 (y, x)도 정수해이므로 2개를 더함
            minus_count += 2
        else:
            # x == y 인 지점 (정확히 45도 방향)
            minus_count += 1

count = (2 * R - 1 - minus_count) * 4
print(count)
