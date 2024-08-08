number = int(input())

A = []
B = []

for _ in range(number):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    
for i in range(number):
    print(A[i] + B[i])