N, K = map(int, input().split())

# 설명에 페르마의 소정리를 이용하여 곱셈의 역원을 구하는 문제
# 라고 써있어서,
# 페르마의 소정리니까 1,000,000,007 이 소수인가 싶어서 확인해봤는데, 소수 맞음.

# 곱셈의 역원 : 그 수와 곱하면 1(항등원)이 되는 수
# 페르마의 소정리에 의해
# p가 소수일 때
# a^(p-1) = 1 (mod p) 

# nCk = n! / (k!(n-k)!)

# 1629를 풀었을 때, A * B % C 를 구하는 걸 분할정복으로 풀었으니까, 이번에도 동일하게 적용하면
# n! * 1/(k!(n-k)!) % 1,000,000,007 을 푸는 게 11401 문제.

# 페르마의 소정리에서
# a^(p-1) % p = 1
# => ( n! / (k!(n-k)!) ) ^ (p-1) % p = 1
# = n! * (k!(n-k)!)^(-1) ^ (p-1) % p = 1
# = n! * (k!(n-k)!)^(p-2) ^ (p-1) % p = 1     # 위 식에서 여기 식으로 유도되는 게 레전드임.

# 그니까
# (A^(-1))^(p-1) % p = (A^(p-2))^(p-1) % p
# 이 성립함.


C = 1000000007

def factorial_mod(n):
    result = 1
    for i in range(2, n+1):
        result *= i
        result %= C
    return result

def recursive_power_mod(A, B):
    if B == 1:
        return A % C
    else:
        temp = recursive_power_mod(A, B // 2)
        if B % 2 == 0:
            return temp ** 2 % C
        else:
            return temp ** 2 * A % C
        
A = factorial_mod(N)
B = factorial_mod(N-K) * factorial_mod(K) % C
result = (A * recursive_power_mod(B, C-2)) % C

print(result)