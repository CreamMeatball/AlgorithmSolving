n = int(input())

# 1,000,000,007 이 소수.

# 페르마의 소정리에서
# a^(p-1) % p = 1
# => ( n! / (k!(n-k)!) ) ^ (p-1) % p = 1
# = n! * (k!(n-k)!)^(-1) ^ (p-1) % p = 1
# = n! * (k!(n-k)!)^(p-2) ^ (p-1) % p = 1     # 위 식에서 여기 식으로 유도되는 게 레전드임.

# 그니까
# (A^(-1))^(p-1) % p = (A^(p-2))^(p-1) % p
# 이 성립함.

modulo = 1000000007

def modulo_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_modulo(1, n) + recursive_modulo(1, n-1)

def recursive_modulo(value, n):
    if n == 1:
        return value % modulo
    else:
        temp = recursive_modulo(value, n // 2)
        if n % 2 == 0: # 짝수이면
            return temp ** 2 % modulo
        else: # 홀수이면
            return temp ** 2 * value % modulo
        
print(modulo_fibonacci(n))