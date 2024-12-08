N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sort = sorted(A)
B_sort = sorted(B, reverse=True)

result = 0
for i in range(N):
    result += A_sort[i] * B_sort[i]
    
print(result)