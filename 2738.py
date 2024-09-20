N, M = map(int, input().split())

A = [0 for _ in range(N)]
B = [0 for _ in range(N)]

for i in range(N):
    A[i] = list(map(int, input().split()))
    
for i in range(N):
    B[i] = list(map(int, input().split()))

convolution = [[] for _ in range(N)]

for i in range(N):
    for j in range(M):
        convolution[i].append(A[i][j] + B[i][j])

# print(A)
# print(B)
# print(convolution)

for i in range(N):
    for j in range(M):
        print(convolution[i][j], end=" ")
    print()