N, M = map(int, input().split())
N_list = []
M_list = []
for i in range(N):
    N_list.append(input())
for i in range(M):
    M_list.append(input())
    
# print(N_list)
# print(M_list)
    
count = 0

for i in M_list:
    if i in N_list:
        count += 1
        
print(count)