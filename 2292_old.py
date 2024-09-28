# 0 : 1
# 1 : 2 3 4 5 6 7
# 2 : 8 9 10 11 12 13 14 15 16 17 18 19
# 3 : 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37
# 4 : 38 39 40 41 42 ~ 61

# 더해지는 양 : 6 12 18 24 ...

N = int(input())

branch = []
branch.append(1)
for i in range(1,N+1):
    branch.append(branch[i-1] + 6*i)
    
# print(branch)

for i in range(len(branch)):
    # print("constrast with ", i)
    if branch[i] >= N:
        print(i+1)
        break
