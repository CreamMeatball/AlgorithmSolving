# 피보나치를 행렬로 표현하기
# [1  1]ⁿ  =  [F(n+1)  F(n)]
# [1  0]      [F(n)    F(n-1)]

# 과정
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) (n ≥ 2)

# [F(n+1)]   =  [1  1]  ×  [F(n)]       =  [1  1]  ×  [F(n)]
# [F(n)]        [1  0]     [F(n-1)]        [1  0]     [F(n-1)]

# [F(n+1)]   =  [1  1]  ×  [1  1]  ×  [F(n-1)]   =  [1  1]²  ×  [F(n-1)]
# [F(n)]        [1  0]     [1  0]     [F(n-2)]      [1  0]      [F(n-2)]

# [F(n+1)]   =  [1  1]ⁿ  ×  [F(1)]   =  [1  1]ⁿ  ×  [1]
# [F(n)]        [1  0]      [F(0)]      [1  0]      [0]

# [1  1]ⁿ  =  [F(n+1)  F(n)]
# [1  0]      [F(n)    F(n-1)]

# 시간 복잡도 비교
# 1. 일반 재귀 구현: O(N^2)
# 2. 메모이제이션 재귀/반복문 구현: O(n)
# 3. 행렬곱 + 분할정복: O(logn)


def matrix_multiply(A, B, mod): # 행렬곱
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C

def matrix_power(A, n, mod): # 행렬의 n제곱. 근데 이제 분할정복을 곁들인
    if n == 1:
        return A
    if n % 2 == 0: # 짝수일 때
        half = matrix_power(A, n // 2, mod)
        return matrix_multiply(half, half, mod)
    else: # 홀수일 때
        half = matrix_power(A, n // 2, mod)
        return matrix_multiply(matrix_multiply(half, half, mod), A, mod)

def fibonacci(n, mod): # 행렬곱을 이용한 피보나치 구하기. 근데 이제 10억7로 나눔을 곁들인
    if n == 0:
        return 0
    
    A = [[1, 1], [1, 0]]
    
    if n == 1:
        return A[0][1]  # F(1) = 1
        
    result_matrix = matrix_power(A, n, mod)
    
    return result_matrix[0][1]

n = int(input())
modulo = 1000000007
print(fibonacci(n, modulo))