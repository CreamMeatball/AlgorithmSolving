# PyPy3

N = int(input())
R = N // 2
R_sq = R * R

minus_count = 0

# x와 y를 양 끝에 두고 좁혀오는 투 포인터 방식 사용 (시간 초과 때문에 써야됨)
x = 1
y = R - 1

while x <= y:
    val = x*x + y*y

    # 시간 초과 때문에, 사분면 중 하나만 보는 걸 넘어 1/8만 보기.
    if val == R_sq:
        if x < y:
            # (x, y)가 정수해면 대칭점인 (y, x)도 정수해이므로 2개를 더함
            minus_count += 2
        else:
            # x == y 인 지점 (정확히 45도 방향)
            minus_count += 1
        x += 1
        y -= 1
    elif val < R_sq:
        # 원 안쪽에 있으므로 x를 키워서 원주에 가깝게 이동
        x += 1
    else:
        # 원 바깥에 있으므로 y를 줄여서 원주에 가깝게 이동
        y -= 1

count = (2 * R - 1 - minus_count) * 4

print(count)
