N = int(input())
P_i = list(map(int, input().split()))
total = 0
i = 0

P_i.sort()

for i in range(N):
    for j in range(i+1):
        total += P_i[j]
        
print(total)