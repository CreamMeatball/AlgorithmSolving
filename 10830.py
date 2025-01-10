import sys

input_data = sys.stdin.readline

N, B = map(int, input_data().rstrip().split())

A = []

for _ in range(N):
    A.append(list(map(int, input_data().rstrip().split())))
    
def matrix_mul_divide(A, A2):
    result = [[0] * N for _ in range(N)]
    
    for n in range(N):
        for k in range(N):
            for m in range(N):
                result[n][k] += A[n][m] * A2[m][k] % 1000
    
    return result

def matrix_pow(A, exponent):
    if exponent == 1:
        return A
    elif exponent % 2 == 0:
        return matrix_pow(matrix_mul_divide(A, A), exponent // 2) # 여기를 통해 A^A 된 애가 다시 matrix_pow로 들어가서, (A^2)^(A^2) 이 됨.
    else:
        return matrix_mul_divide(A, matrix_pow(A, exponent - 1))
    
for row in matrix_pow(A, B):
    row =  list(map(int, row))
    print(' '.join(map(str, [element % 1000 for element in row])))
    