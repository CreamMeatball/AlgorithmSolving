# N = int(input())
# Nlist = list(map(int, input().split()))
# M = int(input())
# Mlist = list(map(int, input().split()))

# for m in Mlist:
#     if m in Nlist:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

N = int(input())
Nlist = [0 for i in range(20000001)]
temp = list(map(int, input().split()))
for t in temp:
    Nlist[t+10000000] = 1
    
M = int(input())
Mlist = list(map(int, input().split()))
for m in Mlist:
    if Nlist[m+10000000] == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')