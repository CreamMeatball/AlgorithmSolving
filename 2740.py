import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().rstrip().split())
A = []

for _ in range(N):
    A.append(list(map(int, input_data().rstrip().split())))
    
M, K = map(int, input_data().rstrip().split())
B = []

for _ in range(M):
    B.append(list(map(int, input_data().rstrip().split())))
    
# [1, 2]
# [3, 4]
# [5, 6]

# [-1, -2, 0]
# [0, 0, 3]
    
result = [[0] * K for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += A[n][m] * B[m][k]
            
# print(result)

for row in result:
    print(' '.join(map(str, row)))