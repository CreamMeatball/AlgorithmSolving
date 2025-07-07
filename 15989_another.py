# DP 말고 다른 방식으로도 풀어보기

import sys

input_ = sys.stdin.readline

T = int(input_().rstrip())

for _ in range(T):
    n = int(input_().rstrip())
    count = 0
    n_3 = n // 3
    for i in range(n_3 + 1):
        n_2 = (n - 3 * i) // 2
        # n_2 개만큼 2원을 사용하고, 나머지 금액은 1원으로 채워넣기
        count += n_2 + 1 # 2원을 0개 쓰는 경우까지 더함
    print(count)
