N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))

N_dict = {}
for n in Nlist:
    N_dict[n] = 1
    
for m in Mlist:
    if m in N_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')