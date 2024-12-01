N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
for a in A:
    print(sorted_A.index(a), end=' ')
    sorted_A[sorted_A.index(a)] = None
    