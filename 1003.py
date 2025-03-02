import sys

# 피보나치 수열을 재귀로 풀면 시간 초과가 발생한다.
# 피보나치를 구현하지 않는 DP 문제.

# count_0 = 0
# count_1 = 0

# def fibonacci(n):
#     global count_0, count_1
#     if n == 0:
#         count_0 += 1
#         return 0
#     elif n == 1:
#         count_1 += 1
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    
input_data = sys.stdin.readline

T = int(input_data())

for _ in range(T):
    N = int(input_data())
    # fibonacci(N)
    # print(count_0, count_1)
    # count_0, count_1 = 0, 0
    a = [1, 0]
    b = [0, 1]
    if N == 0:
        print(a[0], a[1])
    elif N == 1:
        print(b[0], b[1])
    else:
        c = [a[0] + b[0], a[1] + b[1]]
        for i in range(2, N):
            a = b
            b = c
            c = [a[0] + b[0], a[1] + b[1]]
        print(c[0], c[1])
        
    # 규칙성을 좀 더 면밀히 파악하면
    # 아래와 같이 더 간단하게도 구현 가능
    # a, b = 1, 0
    # for _ in range(N):
    #     a, b = b, a + b
    # print(a, b)
    
# f(0) = 1 / 0
# f(1) = 0 / 1
# f(2) = f(1) + f(0) = 1 / 1
# f(3) = f(2) + f(1) = 1 / 2
# f(4) = f(3) + f(2) = 2 / 3
# f(5) = f(4) + f(3) = 3 / 5
# f(6) = f(5) + f(4) = 5 / 8
# f(7) = f(6) + f(5) = 8 / 13