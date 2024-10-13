N = int(input())

input_data = input().split()

N_dict = {}
for data in input_data:
    data = int(data)
    if data in N_dict:
        N_dict[data] += 1
    else:
        N_dict[data] = 1
        
# print(N_dict)

M = int(input())

M_list = list(map(int, input().split()))

for m in M_list:
    if m in N_dict:
        print(N_dict[m], end=' ')
    else:
        print(0, end=' ')

