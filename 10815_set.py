N = int(input())
Nset = set(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))

    
for m in Mlist:
    if m in Nset:
        print(1, end=' ')
    else:
        print(0, end=' ')