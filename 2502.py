D, K = map(int, input().split())

# 첫날 준 떡 A, 둘째날 준 떡 B 라고 할 때
# 날마다 주는 떡의 개수는 아래와 같음.
# A, B, A+B, A+2B, 2A+3B, 3A+5B, 5A+8B, 8A+13B, 13A+21B, ...

fibonacci = [
    [0, 0], # dummy at init
    [1, 0],
    [0, 1]
]

for i in range(3, D + 1):
    fibonacci[0] = fibonacci[1]
    fibonacci[1] = fibonacci[2]
    fibonacci[2] = [fibonacci[0][0] + fibonacci[1][0], fibonacci[0][1] + fibonacci[1][1]]
    
# D일째에 주어야 하는 떡의 개수 K = a_coeff*A + b_coeff*B
a_coeff = fibonacci[2][0]
b_coeff = fibonacci[2][1]

# A와 B 값을 찾기 (1 ≤ A ≤ B)
for A in range(1, K):
    # K - a_coeff*A가 b_coeff로 나누어 떨어지는지 확인
    if (K - a_coeff*A) % b_coeff == 0:
        B = (K - a_coeff*A) // b_coeff
        if A <= B: # 이 조건이 무조건 있어야 함. 더 전날에 준 떡 개수가 같거나 작아야하기 떄문.
            print(A)
            print(B)
            break