import sys

input_data = sys.stdin.readline

N, M = map(int, input_data().rstrip().split())

matrixA = []
for _ in range(N):
    matrixA.append(list(map(int, list(input_data().rstrip()))))
    
matrixB = []
for _ in range(N):
    matrixB.append(list(map(int, list(input_data().rstrip()))))
    
count = 0
    
def flip(x, y, matrix):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
            
def isSame(matrixA, matrixB):
    for i in range(N):
        for j in range(M):
            if matrixA[i][j] != matrixB[i][j]:
                return False
    return True

for i in range(N - 2):
    for j in range(M - 2):
        if matrixA[i][j] != matrixB[i][j]:
            flip(i, j, matrixA)
            count += 1

if isSame(matrixA, matrixB):
    print(count)
else:
    print(-1)