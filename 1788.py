n = int(input())

# 이게 해보니까
# 음수 피보나치에서는
# 부호가 - + 교차되는데
# 절대값 자체는 양수 피보나치랑 똑같이 가네

MOD = 1000000000

abs_n = abs(n)

a, b, c = 0, 1, 1

if abs_n == 0:
    print(0)
    print(0)
else:
    for _ in range(2, abs_n + 1):
        c = (a + b) % MOD
        a, b = b, c
    if n > 0:
        print(1)
    else: # n이 음수인 경우
        if abs_n % 2 == 0: # 짝수 음수마다 - 부호가 나옴. -2, -4, -6, ...
            print(-1)
        else:
            print(1)
    
    print(c)