x, y, c = map(float, input().split())

# 이게 수학적으로 완전히 방정식을 풀어야 되는 줄 알았는데
# 식 정리한 뒤에, 밑변 값 조금씩 변화시키면서 정리된 식을 만족하는 값 찾기.

# [참고]: https://velog.io/@qlql323/%EB%B0%B1%EC%A4%80-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-2022-%EC%82%AC%EB%8B%A4%EB%A6%AC

# 식을 정리하면
# c = (h1 * h2) / (h1 + h2)       # <- 이거 도출이 어려움.. 닮을비 식이랑 w = w1 + w2 이용해서 도출.
# h1 = sqrt(x^2 - w^2)
# h2 = sqrt(y^2 - w^2)

# 여기서 x, y 는 상수이므로,
# 미지수 w의 컨트롤을 통해 h1, h2가 결정됨.
# 그리고 곧 h1, h2가 결정됨으로 인해 c가 결정됨.
# 결국, 미지수 w의 컨트롤로 인해 c가 결정됨.
# (w가 증가하면 c가 감소함. 반비례 관계)
# 왜나면 w가 커지면 h1, h2가 작아지고, c = (h1 * h2) / (h1 + h2) 는 역수로 뒤집으면 1/c = 1/h2 + 1/h1 이고, 이 때 h1과 h2가 작아지면 c가 작아지기 때문.
# 더 쉽게는 기하적으로 보면 됨. 그림에서 w가 작아지면 직관적으로 c가 커짐.

# -> w 조금씩 변화해보면서 주어진 c랑 맞는지 (오차 범위 안에 드는지) 확인하면 됨.

high = min(x, y) # w's upper bound. w가 x 또는 y보다 작을테니, w의 최대값을 min(x, y)로 설정
low = 0 # w's lower bound
# high, low는 w를 binary search 해서 찾기 위함. binary search의 left, right 값.
answer = 0

while low + 0.001 <= high: # 오차 범위보다 작아질 때까지 탐색
    w = (low + high) / 2
    h1 = (x**2 - w**2)**0.5
    h2 = (y**2 - w**2)**0.5
    c_hat = (h1 * h2) / (h1 + h2)
    if c_hat >= c:
        # w와 c는 반비례 관계기에(위에서 설명), 현재의 w 값에서 도출된 c 예측값이 실제 c보다 크다면, 현재 w가 정답보다 작은 w라는 뜻이므로,
        # low를 높여서 다음 iteration의 (다음에 계산해볼) w의 값을 높여줌.
        answer = w
        low = w
    else:
        high = w

print(f"{answer:.3f}")