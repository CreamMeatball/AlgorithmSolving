S = list(input())
A = 'abcdefghijklmnopqrstuvwxyz'

for a in A:
    if a in S:
        print(S.index(a), end =' ')
    else:
        print(-1, end=' ')